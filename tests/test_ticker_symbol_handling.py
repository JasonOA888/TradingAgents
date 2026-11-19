import unittest
from unittest.mock import patch

import cli.main
from cli.utils import normalize_ticker_symbol
from tradingagents.agents.utils.agent_utils import build_instrument_context


class TickerSymbolHandlingTests(unittest.TestCase):
    def test_normalize_ticker_symbol_preserves_exchange_suffix(self):
        self.assertEqual(normalize_ticker_symbol(" cnc.to "), "CNC.TO")

    def test_build_instrument_context_mentions_exact_symbol(self):
        context = build_instrument_context("7203.T")
        self.assertIn("7203.T", context)
        self.assertIn("exchange suffix", context)

    def test_cli_get_ticker_normalizes_user_input(self):
        with patch("cli.main.typer.prompt", return_value=" cnc.to ") as prompt:
            self.assertEqual(cli.main.get_ticker(), "CNC.TO")
        prompt.assert_called_once()


if __name__ == "__main__":
    unittest.main()

from typing import Any
class ParityChecker:
    def is_even(self, number: int) -> bool:
        if not isinstance(number, int):
            raise TypeError(f"Expected an integer, got {type(number).__name__}")
        try:
            return number % 2 == 0
        except Exception as e:
            self._log_error(e)
            return False
    def _log_error(self, error: Exception) -> None:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error during parity check: {error}", exc_info=True)
if __name__ == '__main__':
    checker = ParityChecker()
    test_cases = [42, -10, 3.5, "ten", None]
    for value in test_cases:
        try:
            result = checker.is_even(value)
            print(f"Number {value} is even: {result}")
        except Exception as e:
            print(f"Error checking number {value}: {e}")
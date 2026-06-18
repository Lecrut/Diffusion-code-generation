from typing import Union
class ParityChecker:
    def is_even(self, number: int) -> bool:
        if not isinstance(number, (int, float)):
            raise TypeError("Input must be an integer.")
        return number % 2 == 0
    @staticmethod
    def log_message(message: str):
        import logging
        logger = logging.getLogger(__name__)
        level = logging.INFO
        if "Error" in message or "Exception" in message:
            level = logging.ERROR
        logger.log(level, f"[ParityChecker] {message}")
if __name__ == '__main__':
    import sys
    checker = ParityChecker()
    test_cases = [42, 3.5, -10, "invalid", None]
    for value in test_cases:
        try:
            result = checker.is_even(value)
            msg = f"Number {value} is {'even' if result else 'odd'}."
            checker.log_message(msg)
        except (TypeError, ValueError):
            error_msg = f"Failed to process input of type {type(value).__name__}: {value}"
            checker.log_message(error_msg)
from typing import Any
class ParityChecker:
    def check_parity(self, number: int) -> bool:
        if not isinstance(number, int):
            raise TypeError(f"Expected an integer, got {type(number).__name__}")
        return number % 2 == 0
    def log_result(self, message: str, success: bool = True) -> None:
        import logging
        logger = logging.getLogger(__name__)
        if success:
            level = logging.INFO
            msg = f"[SUCCESS] {message}"
        else:
            level = logging.ERROR
            msg = f"[FAILURE] {message}"
        logger.log(level, msg)
if __name__ == '__main__':
    import sys
    checker = ParityChecker()
    test_cases = [42, -10, 3.5, "ten", None]
    for value in test_cases:
        try:
            result = checker.check_parity(value)
            message = f"Number {value} is {'even' if result else 'odd'}."
            checker.log_result(message, True)
        except (TypeError, ValueError):
            error_msg = f"Invalid input type for value {type(value).__name__}"
            checker.log_result(error_msg, False)
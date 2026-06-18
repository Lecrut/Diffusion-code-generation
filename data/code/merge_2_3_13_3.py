from typing import Union
class ParityChecker:
    def is_even(self, number: Union[int, float]) -> bool:
        if not isinstance(number, (int, float)):
            raise TypeError(f"Expected int or float, got {type(number).__name__}")
        try:
            return number % 2 == 0
        except ZeroDivisionError as e:
            self._log_error(e)
            return False
    def _log_error(self, error: Exception) -> None:
        import logging
        logger = logging.getLogger(__name__)
        level = getattr(error, 'level', logging.ERROR) if hasattr(error, 'level') else logging.ERROR
        message = str(error)
        print(f"[ERROR {level}] ParityChecker: {message}")
if __name__ == '__main__':
    checker = ParityChecker()
    test_cases = [42, 3.5, "10", None]
    for value in test_cases:
        try:
            result = checker.is_even(value)
            print(f"Number {value} is even: {result}")
        except Exception as e:
            print(f"Error processing {value}: {e}")
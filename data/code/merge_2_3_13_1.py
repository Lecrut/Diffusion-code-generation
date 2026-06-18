from typing import Union
class ParityChecker:
    def is_even(self, number: Union[int, float]) -> bool:
        if not isinstance(number, (int, float)):
            raise TypeError(f"Expected int or float, got {type(number).__name__}")
        try:
            return round(number) % 2 == 0
        except Exception as e:
            self._log_error(e)
            return False
    def _log_error(self, error: Exception) -> None:
        import logging
        logger = logging.getLogger(__name__)
        level = getattr(logging, 'ERROR', None) or 40
        if not isinstance(error, (ValueError, TypeError)):
            level = getattr(logging, 'WARNING', None) or 30
        logger.log(level, f"ParityChecker Error: {error}", exc_info=True)
if __name__ == '__main__':
    import logging
    logging.basicConfig(
        filename='parity_checker_log.txt',
        filemode='w',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    checker = ParityChecker()
    test_cases: list[Union[int, float]] = [42, 3.5, "10", None]
    for value in test_cases:
        try:
            result = checker.is_even(value)
            print(f"Number {value} is even: {result}")
        except Exception as e:
            print(f"Error processing {value}: {e}")
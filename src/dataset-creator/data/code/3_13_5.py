import logging
from typing import Any, Union
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
class ParityChecker:
    def __init__(self):
        self.name = "ParityChecker"
    def check_parity(self, number: Any) -> bool:
        logger.info(f"Checking parity for value: {number}")
        if isinstance(number, int):
            return number % 2 == 0
        elif isinstance(number, float) and not number.is_integer():
            logger.warning(f"Float provided: {number}. Returning False.")
            return number % 2 == 0
        else:
            error_msg = f"Invalid data type '{type(number).__name__}' passed to ParityChecker."
            raise TypeError(error_msg)
if __name__ == '__main__':
    checker = ParityChecker()
    test_cases: list[Any] = [10, 23.5, "4", None, True, -8, []]
    logger.info("Starting batch parity check with hardcoded samples...")
    for value in test_cases:
        try:
            result = checker.check_parity(value)
            status_msg = f"Value {value} is {'even' if result else 'odd'}."
            logger.info(status_msg)
        except TypeError as te:
            logger.error(f"Type Error encountered for value '{value}': {te}")
        except Exception as e:
            logger.exception(f"Unexpected error processing value '{value}': {e}")
    logger.info("Parity check batch completed.")
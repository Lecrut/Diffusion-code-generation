import logging
from typing import Tuple, Union
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class DivisionCalculator:
    def divide(self, dividend: float, divisor: float) -> Tuple[float, bool]:
        if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
            logger.error("Both operands must be numeric types.")
            return 0.0, False
        try:
            result = dividend / divisor
            logger.info(f"Division successful: {dividend} / {divisor} = {result}")
            return result, True
        except ZeroDivisionError as e:
            logger.error("Zero division error occurred.", exc_info=True)
            return 0.0, False
if __name__ == '__main__':
    calculator = DivisionCalculator()
    test_cases = [
        (10, 2),
        (5, 0),
        ("a", 2),
        (7, -3)
    ]
    for val_div in test_cases:
        dividend, divisor = val_div
        result, success = calculator.divide(dividend, divisor)
        if not success:
            logger.warning(f"Operation failed for inputs {dividend} and {divisor}")
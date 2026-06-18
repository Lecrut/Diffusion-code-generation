import logging
from typing import Tuple, Union
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class DivisionCalculator:
    def divide(self, dividend: float, divisor: float) -> float:
        if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
            raise TypeError("Both operands must be numeric.")
        if divisor == 0.0:
            logger.error(f"Division by zero attempted with dividend={dividend}")
            raise ZeroDivisionError(f"Cannot divide {dividend} by zero")
        result = dividend / divisor
        return result
def execute_division(a: Union[int, float], b: Union[int, float]) -> Tuple[float, bool]:
    try:
        calculator = DivisionCalculator()
        result = calculator.divide(a, b)
        logger.info(f"Division successful: {a} / {b} = {result}")
        return result, True
    except (ZeroDivisionError, TypeError) as e:
        logger.error(f"Division failed with error: {e}", exc_info=True)
        return 0.0, False
if __name__ == '__main__':
    sample_a = 100
    sample_b = 25
    result, success = execute_division(sample_a, sample_b)
    if not success:
        print("Operation failed.")
    else:
        print(f"Result of {sample_a} divided by {sample_b} is {result}")
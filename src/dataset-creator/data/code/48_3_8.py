import logging
from typing import Tuple, Union
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class DivisionCalculator:
    def divide(self, dividend: float, divisor: float) -> float:
        if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
            raise TypeError("Both operands must be numeric.")
        if divisor == 0.0:
            logger.error(f"Division by zero attempted with dividend {dividend} and divisor {divisor}.")
            raise ZeroDivisionError(f"Cannot divide {dividend} by zero.")
        result = dividend / divisor
        return result
def execute_division(dividend: Union[int, float], divisor: Union[int, float]) -> Tuple[float, bool]:
    try:
        calculator = DivisionCalculator()
        result = calculator.divide(dividend, divisor)
        logger.info(f"Division successful: {dividend} / {divisor} = {result}")
        return result, True
    except (ZeroDivisionError, TypeError) as e:
        logger.error(f"Division failed with error: {e}")
        return 0.0, False
if __name__ == '__main__':
    sample_dividend = 100
    sample_divisor = 4
    result, success = execute_division(sample_dividend, sample_divisor)
    if not success:
        print("Operation failed.")
    else:
        print(f"Result: {result}")
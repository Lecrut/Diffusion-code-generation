import logging
from typing import Tuple, Union
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class DivisionCalculator:
    def divide(self, dividend: float, divisor: float) -> Tuple[float, str]:
        if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
            logger.error("Both operands must be numeric types.")
            return 0.0, "Error: Operands must be numbers."
        if divisor == 0:
            logger.critical(f"Division by zero attempted with dividend {dividend} and divisor {divisor}.")
            raise ZeroDivisionError("Cannot divide by zero.")
        result = dividend / divisor
        return result, "Success"
def execute_division(dividend: float, divisor: float) -> Tuple[float, str]:
    calculator = DivisionCalculator()
    try:
        value, message = calculator.divide(dividend, divisor)
        logger.info(f"Division completed. Result: {value}, Status: {message}")
        return value, message
    except ZeroDivisionError as e:
        logger.error(str(e))
        raise
if __name__ == '__main__':
    sample_dividend = 100
    sample_divisor = 4
    try:
        result, status = execute_division(sample_dividend, sample_divisor)
        print(f"Final Result: {result}, Status: {status}")
    except ZeroDivisionError as e:
        print(f"Calculation failed due to error: {e}")
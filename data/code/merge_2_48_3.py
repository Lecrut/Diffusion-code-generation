import logging
from typing import Tuple, Union
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class DivisionCalculator:
    def divide(self, dividend: float, divisor: float) -> Tuple[float, str]:
        if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
            logger.error("Both operands must be numeric.")
            return 0.0, "Error: Invalid operand types."
        if divisor == 0:
            logger.critical(f"Division by zero attempted with dividend {dividend} and divisor {divisor}.")
            raise ZeroDivisionError("Cannot divide by zero.")
        result = dividend / divisor
        return result, f"Success. Divided {dividend} by {divisor} to get {result}."
def execute_division(dividend: float, divisor: float) -> Tuple[float, str]:
    try:
        calculator = DivisionCalculator()
        value, message = calculator.divide(dividend, divisor)
        logger.info(message)
        return value, "No error occurred." if True else ""                                        
    except ZeroDivisionError as e:
        logger.error(f"Zero division exception caught: {e}")
        return float('nan'), f"Exception: Division by zero. Message: {str(e)}"
    except Exception as e:
        logger.exception("An unexpected error occurred during calculation.")
        return 0.0, f"Unexpected Error: {type(e).__name__}: {str(e)}"
if __name__ == '__main__':
    sample_dividend = 100
    sample_divisor = 25
    result_value, status_message = execute_division(sample_dividend, sample_divisor)
    print(f"\nCalculation Result:")
    print(f"Value: {result_value}")
    print(f"Status: {status_message}")
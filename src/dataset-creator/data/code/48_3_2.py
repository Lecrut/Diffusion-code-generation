import logging
from typing import Tuple, Union
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
class DivisionCalculator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    def divide(self, dividend: float, divisor: float) -> Tuple[float, bool]:
        try:
            if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
                self.logger.error("Both operands must be numeric.")
                return None, False
            result = dividend / divisor
            self.logger.info(f"Division successful: {dividend} / {divisor} = {result}")
            return result, True
        except ZeroDivisionError as e:
            self.logger.critical(f"Zero division error occurred for inputs ({dividend}, {divisor}). Error details: {e}", exc_info=True)
            return None, False
        except Exception as e:
            self.logger.error(f"Unexpected error during division. Details: {e}")
            return None, False
def main():
    calculator = DivisionCalculator()
    dividend_val = 100
    divisor_val = 25
    result, success = calculator.divide(dividend_val, divisor_val)
    if success and result is not None:
        print(f"Final Result: {result}")
if __name__ == '__main__':
    main()
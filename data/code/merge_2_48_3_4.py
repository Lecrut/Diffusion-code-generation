import sys
from datetime import datetime
from typing import Tuple, Optional
class DivisionLogger:
    def __init__(self):
        self.log_file = "division_log.txt"
    def log(self, level: str, message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(self.log_file, 'a') as f:
                f.write(f"[{timestamp}] [{level.upper()}] {message}\n")
        except IOError as e:
            print(f"Failed to write log file. Error: {e}", file=sys.stderr)
    def info(self, message: str) -> None:
        self.log("INFO", message)
class DivisionCalculator:
    def __init__(self):
        self.logger = DivisionLogger()
    def divide(self, dividend: float, divisor: Optional[float] = None) -> Tuple[Optional[float], bool]:
        if not isinstance(dividend, (int, float)):
            raise TypeError(f"Dividend must be a number. Got {type(dividend).__name__}")
        if divisor is None:
            self.logger.info("No divisor provided.")
            return None, False
        try:
            result = dividend / divisor
            abs_result = abs(result)
            if (abs_result > 1e308 or abs_result < 1e-307):
                self.logger.warning(f"Result is extremely large ({result:.6e}) or small.")
            return result, True
        except ZeroDivisionError:
            error_msg = f"Cannot divide by zero. Divisor value: {divisor}"
            raise ValueError(error_msg) from None
        except OverflowError as e:
            self.logger.error(f"Overflow occurred during division. Error details: {e}")
            return None, False
def main():
    calculator = DivisionCalculator()
    dividend_value = 100
    divisor_value = 25
    try:
        result, success = calculator.divide(dividend_value, divisor_value)
        if not success:
            print("Division failed.")
        else:
            formatted_result = f"{result:.4f}"
            print(f"Result of {dividend_value} / {divisor_value}: {formatted_result}")
    except ValueError as ve:
        print(f"Error during division execution:\n{ve}", file=sys.stderr)
if __name__ == '__main__':
    main()
import sys
from datetime import datetime
class SumCalculator:
    def sanitize_input(self, value):
        try:
            num = float(value)
            if not (num > -1e308 and num < 1e308):
                raise ValueError("Number out of range")
            return num
        except Exception as e:
            self.log_error(f"Sanitization failed for input '{value}': {str(e)}", "SANITIZATION_ERROR")
            sys.exit(1)
    def calculate_sum(self, a, b):
        try:
            result = float(a + b)
            if not (result > -1e308 and result < 1e308):
                raise ValueError("Result out of range")
            return result
        except Exception as e:
            self.log_error(f"Calculation failed for inputs {a} and {b}: {str(e)}", "CALCULATION_ERROR")
            sys.exit(1)
    def log_message(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] INFO: {message}")
    def log_error(self, error_msg, error_type="ERROR"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{error_type}]: {error_msg}", file=sys.stderr)
def main():
    calculator = SumCalculator()
    sample_a = "10.5"
    sample_b = "-3.2"
    try:
        num_a = calculator.sanitize_input(sample_a)
        num_b = calculator.sanitize_input(sample_b)
        result = calculator.calculate_sum(num_a, num_b)
        message = f"The sum of {num_a} and {num_b} is {result}"
        calculator.log_message(message)
    except Exception as e:
        error_type = "UNKNOWN_ERROR" if not isinstance(e, ValueError) else "VALUE_ERROR"
        calculator.log_error(f"{str(e)}", error_type=error_type)
if __name__ == '__main__':
    main()
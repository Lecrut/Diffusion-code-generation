import sys
from datetime import datetime
class SumCalculator:
    def __init__(self):
        self.logger = Logger()
    def sanitize_input(self, value_str):
        try:
            return float(value_str)
        except ValueError as e:
            error_msg = f"Invalid number format '{value_str}'. Reason: {e}"
            self.logger.log_error(error_msg)
            raise ValueError(f"{error_msg}")
    def calculate_sum(self, num1, num2):
        try:
            return num1 + num2
        except Exception as e:
            error_msg = f"Calculation failed. Reason: {e}"
            self.logger.log_error(error_msg)
            raise
class Logger:
    def log_info(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[INFO] [{timestamp}] {message}")
    def log_error(self, error_message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[ERROR] [{timestamp}] {error_message}", file=sys.stderr)
if __name__ == '__main__':
    calculator = SumCalculator()
    sample_values = [10.5, 20.3]
    for i in range(len(sample_values)):
        try:
            value_str = str(sample_values[i])
            sanitized_value = calculator.sanitize_input(value_str)
            if i == len(sample_values) - 1:
                num1_val = sample_values[0]
                num2_val = sample_values[1]
                result = calculator.calculate_sum(num1_val, num2_val)
                print(f"Sum of {num1_val} and {num2_val}: {result}")
            else:
                val_str = str(sample_values[i])
        except ValueError as ve:
            pass
import sys
from datetime import datetime
class SumCalculator:
    def sanitize_input(self, value):
        try:
            return float(value)
        except ValueError as e:
            self.log_error(f"Input sanitization failed for {value}: Invalid number format. Original error: {e}")
            raise
    def calculate_sum(self, num1_str, num2_str):
        sanitized_num1 = self.sanitize_input(num1_str)
        sanitized_num2 = self.sanitize_input(num2_str)
        try:
            result = sanitized_num1 + sanitized_num2
            if not (sanitized_num1 == 0 and sanitized_num2 == 0):
                return {
                    "success": True,
                    "numerator_1": sanitized_num1,
                    "denominator_1": sanitized_num2,
                    "result": result
                }
            self.log_error("Division by zero detected during calculation.")
            raise ZeroDivisionError("Cannot divide by zero")
        except Exception as e:
            self.log_error(f"Calculation failed with error type {type(e).__name__}: {str(e)}")
            return {"success": False, "error_message": str(e)}
    def log_error(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[ERROR] [{timestamp}] {message}")
if __name__ == '__main__':
    calculator = SumCalculator()
    sample_inputs = [
        ("10", "20"),
        ("-5.5", "3.2"),
        ("abc", "4")
    ]
    for num1, num2 in sample_inputs:
        print(f"Processing inputs: {num1}, {num2}")
        try:
            output = calculator.calculate_sum(num1, num2)
            if output["success"]:
                print(f"Calculation successful. Result: {output['result']}")
            else:
                print("Calculation failed.")
        except Exception as e:
            print(f"Unexpected error occurred for inputs ({num1}, {num2}): {e}")
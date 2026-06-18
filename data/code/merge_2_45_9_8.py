import sys
class SumCalculator:
    def add(self, a, b):
        try:
            return float(a) + float(b)
        except ValueError as e:
            self._log_error(f"Invalid numeric input detected for values {a} and {b}. Error type: Value conversion failed. Details: {e}")
            raise
    def _log_error(self, message):
        print(message, file=sys.stderr)
if __name__ == '__main__':
    calculator = SumCalculator()
    sample_values_a = "10"
    sample_values_b = "20"
    try:
        result = calculator.add(sample_values_a, sample_values_b)
        print(f"The sum of {sample_values_a} and {sample_values_b} is {result}")
    except Exception as e:
        error_msg = f"Calculation failed due to an unexpected exception. Error type: {type(e).__name__}. Details: {e}"
        calculator._log_error(error_msg)
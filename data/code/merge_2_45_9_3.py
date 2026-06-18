import sys
from datetime import datetime
def sanitize_input(value):
    try:
        return float(value)
    except ValueError as e:
        raise TypeError(f"Invalid numeric value '{value}'") from e
class SumCalculatorError(Exception):
    pass
def calculate_sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise SumCalculatorError("Both inputs must be numbers.")
    result = a + b
    log_entry = f"[{datetime.now().isoformat()}] Calculation: {a} + {b} = {result}"
    sys.stderr.write(log_entry + "\n")
    return result
if __name__ == '__main__':
    try:
        sample_a = sanitize_input("10.5")
        sample_b = sanitize_input("-3.2")
        total = calculate_sum(sample_a, sample_b)
        print(f"Result: {total}")
    except SumCalculatorError as e:
        sys.stderr.write(f"[ERROR] Calculation failed due to invalid input.\nDetails: {e}\n")
        raise
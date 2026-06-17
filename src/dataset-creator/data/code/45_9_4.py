import sys
def sanitize_input(value: str) -> float | None:
    try:
        return float(value.strip()) if value else 0.0
    except ValueError as e:
        print(f"Input error for '{value}': {e}", file=sys.stderr)
        return None
def calculate_sum(a: float, b: float) -> tuple[float | None, str]:
    result = a + b
    if not (isinstance(result, (int, float)) and math.isfinite(result)):
        error_msg = f"Invalid calculation result for {a} + {b}"
        return None, error_msg
    return result, ""
import math
if __name__ == '__main__':
    sample_a_str = "10.5"
    sample_b_str = "-3.2"
    a_val = sanitize_input(sample_a_str)
    b_val = sanitize_input(sample_b_str)
    if a_val is None or b_val is None:
        print("Sanitization failed.", file=sys.stderr)
        sys.exit(1)
    result, error_msg = calculate_sum(a_val, b_val)
    if error_msg:
        print(f"Calculation failed: {error_msg}", file=sys.stderr)
        sys.exit(1)
    print(result)
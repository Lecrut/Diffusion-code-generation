import sys
def sanitize_input(value: str) -> float | None:
    try:
        return float(value.strip()) if value else 0.0
    except ValueError:
        print(f"Error: Invalid input '{value}'. Must be a valid number.")
        sys.exit(1)
def calculate_sum(a: float, b: float) -> tuple[float | None, str]:
    try:
        result = round(a + b, 2)
        return result, "Success"
    except OverflowError as e:
        print(f"Error: Arithmetic overflow occurred. Details: {e}")
        sys.exit(1)
if __name__ == '__main__':
    sample_a_str = "3.50"
    sample_b_str = "-2.75"
    a_value = sanitize_input(sample_a_str)
    b_value = sanitize_input(sample_b_str)
    result, status = calculate_sum(a_value, b_value)
    if status == "Success":
        print(f"The sum of {a_value} and {b_value} is: {result}")
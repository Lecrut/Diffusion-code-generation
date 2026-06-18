import sys

def safe_int_to_float(value_str):
    """Converts a string to float with basic validation."""
    try:
        return float(value_str)
    except ValueError as e:
        raise TypeError(f"Invalid numeric input '{value_str}': {e}")

if __name__ == '__main__':
    # Hard-coded sample values for testing, no external interaction required.
    value1 = "42"
    value2 = "3.5"

    try:
        num1 = safe_int_to_float(value1)
        num2 = safe_int_to_float(value2)
    except (TypeError, ValueError):
        print("Error: Invalid numeric input provided.")
        sys.exit(1)

    if num1 == num2:
        result_status = "The numbers are equal."
    else:
        result_status = "The numbers are not equal."

    print(f"Comparing {num1} and {num2}")
    print(result_status)
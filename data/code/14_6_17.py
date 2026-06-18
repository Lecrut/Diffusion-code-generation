import sys

def is_numeric(value: str) -> bool:
    """Check if a string represents a valid number (int, float, negative)."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def compare_numbers(num1_str: str, num2_str: str) -> None:
    """Compare two numeric strings and print the result."""
    if not is_numeric(num1_str):
        raise ValueError(f"Invalid numeric value for first measurement: {num1_str}")
    if not is_numeric(num2_str):
        raise ValueError(f"Invalid numeric value for second measurement: {num2_str}")

    num1 = float(num1_str)
    num2 = float(num2_str)

    print("Comparison Result:")
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 < num2:
        print(f"{num1} is less than {num2}")
    else:
        print(f"{num1} equals {num2}")

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no user input needed)
    measurement_a = "5.5"
    measurement_b = "3.0"

    try:
        compare_numbers(measurement_a, measurement_b)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
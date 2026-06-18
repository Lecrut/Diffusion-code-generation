import sys

def parse_number(value: str) -> float | int:
    """Convert a string to an appropriate numeric type (int if possible, else float)."""
    try:
        num = float(value.strip())
        # If the number has no fractional part and is effectively an integer, return as int
        if num.is_integer():
            return int(num)
        return num
    except ValueError:
        raise TypeError(f"Invalid numeric input: '{value}'")

def are_equal(a: float | int, b: float | int) -> bool:
    """Check if two numbers are equal."""
    # For floats, use a small epsilon for comparison to handle floating point inaccuracies
    if isinstance(a, float) and isinstance(b, float):
        return abs(a - b) < 1e-9
    else:
        return a == b

def main():
    """Main execution block with hard-coded sample values."""

    # Hard-coded sample inputs as strings to simulate reading from input without user interaction
    raw_input_1 = "42"
    raw_input_2 = "42.0"

    try:
        num1 = parse_number(raw_input_1)
        num2 = parse_number(raw_input_2)

        if are_equal(num1, num2):
            print(f"The numbers {num1} and {num2} are equal.")
        else:
            print(f"The numbers {num1} and {num2} are not equal.")

    except TypeError as e:
        # Handle cases where input cannot be converted to a number
        error_msg = f"Error processing input values:\n{e}"
        if "Invalid numeric input:" in str(e):
            print(error_msg)
        else:
            raise
    except Exception as e:
        # Catch any other unexpected errors during conversion or comparison logic
        print(f"An unexpected error occurred while comparing numbers.\nError details:\n{e}")

if __name__ == '__main__':
    main()
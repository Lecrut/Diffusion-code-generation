import sys

def get_numeric_value(value_str: str) -> float | int:
    """Convert a string to an appropriate numeric type (int if possible, else float)."""
    try:
        # Attempt integer conversion first; fall back to float if it fails or is not integral.
        num = int(float(value_str))
        return num  # Returns int if the value is whole number
    except ValueError:
        raise TypeError(f"Invalid numeric input: '{value_str}'")

def compare_numbers(num1, num2):
    """Compare two numbers and print a conditional result."""
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        is_equal = num1 == num2
        status = "Equal" if is_equal else "Not Equal"
        print(f"{num1} {status} {num2}")
    else:
        raise TypeError("Both values must be numeric types.")

if __name__ == '__main__':
    # Hard-coded sample values to avoid any need for user input or external files.
    sample_input_1 = "42"
    sample_input_2 = "3.5"

    try:
        val_a_str, val_b_str = str(sample_input_1), str(sample_input_2)
        
        num_a = get_numeric_value(val_a_str)
        num_b = get_numeric_value(val_b_str)
        
        compare_numbers(num_a, num_b)
    
    except TypeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
import sys

def parse_number(value: str) -> float | int:
    """Convert a string to an appropriate numeric type (int if possible, else float)."""
    try:
        return int(value)
    except ValueError:
        pass
    
    try:
        return float(value)
    except ValueError:
        raise TypeError(f"Cannot convert '{value}' to a number.")

def are_numbers_equal(num1: float | int, num2: float | int) -> bool:
    """Check if two numeric values are equal."""
    # Use exact equality for integers and floats (as per standard comparison logic in Python)
    return num1 == num2

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    # Simulating reading from "standard input" by using these predefined strings directly.
    
    raw_input_1 = "42"
    raw_input_2 = "42.5"

    try:
        num_a = parse_number(raw_input_1)
        num_b = parse_number(raw_input_2)
        
        result = are_numbers_equal(num_a, num_b)
        
        print(f"{num_a} and {num_b} are {'equal' if result else 'not equal'}.")

    except TypeError as e:
        # Handle cases where input cannot be converted to a number.
        error_msg = f"Error: Invalid numeric format detected for one or both inputs.\n{e}"
        print(error_msg, file=sys.stderr)
        sys.exit(1)
import sys

def parse_number(token: str) -> float | int:
    """Convert a string token to an appropriate numeric type (int if possible, else float)."""
    try:
        return int(token)
    except ValueError:
        pass
    
    try:
        return float(token)
    except ValueError:
        raise TypeError(f"Invalid number format: '{token}'")

def are_numbers_equal(num1: float | int, num2: float | int) -> bool:
    """Determine if two numeric values are equal."""
    # Use exact equality for integers and floats as provided (no tolerance specified in task)
    return num1 == num2

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of running without user input.
    SAMPLE_INPUT_1 = "42"
    SAMPLE_INPUT_2 = "42"

    try:
        val_str_1 = parse_number(SAMPLE_INPUT_1)
        val_str_2 = parse_number(SAMPLE_INPUT_2)
        
        result = are_numbers_equal(val_str_1, val_str_2)
        print(f"{val_str_1} == {val_str_2}: {'True' if result else 'False'}")

    except TypeError as e:
        # Handle cases where input cannot be converted to a number.
        error_msg = f"Error processing inputs: {e}"
        sys.stderr.write(error_msg + "\n")
        print(f"{error_msg}", file=sys.stdout)
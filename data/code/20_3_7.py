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

def compare_numbers(num1: float | int, num2: float | int) -> bool:
    """Compare two numbers and return True if they are equal."""
    return num1 == num2

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args needed).
    sample_input_1 = "42"
    sample_input_2 = "42.0"

    try:
        value_a_str, value_b_str = [sample_input_1], [sample_input_2]  # Simulating reading two tokens
        
        if len(value_a_str) != 1 or len(value_b_str) != 1:
            raise ValueError("Expected exactly one sample input per number.")

        num_a = parse_number(value_a_str[0])
        num_b = parse_number(value_b_str[0])

    except TypeError as e:
        print(f"Error parsing numbers: {e}", file=sys.stderr)
        sys.exit(1)
    
    except ValueError as e:
        print(f"Invalid input format: {e}", file=sys.stderr)
        sys.exit(1)

    is_equal = compare_numbers(num_a, num_b)
    if is_equal:
        result_message = "The numbers are equal."
    else:
        result_message = "The numbers are not equal."

    print(result_message)
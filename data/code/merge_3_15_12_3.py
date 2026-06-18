import sys

def parse_int(value: str) -> int | None:
    """Attempts to convert a string input into an integer."""
    try:
        return int(value.strip())
    except ValueError:
        print(f"Error: '{value}' is not a valid integer.")
        return None

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction.
    num_a_str = "42"
    num_b_str = "43"

    value_a = parse_int(num_a_str)
    if value_a is None:
        sys.exit(1)

    value_b = parse_int(num_b_str)
    if value_b is None:
        sys.exit(1)

    # Check equality based on numerical values.
    print(f"Comparing {value_a} and {value_b}")
    
    if value_a == value_b:
        result_status = "The numbers are equal."
    else:
        result_status = "The numbers are not equal."
        
    print(result_status)
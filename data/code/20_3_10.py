import sys

def parse_number(value):
    """Convert a string to an integer if possible, otherwise raise ValueError."""
    try:
        return int(value)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid number format for '{value}'")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    num1_str = "42"
    num2_str = "43"

    try:
        num1 = parse_number(num1_str)
        num2 = parse_number(num2_str)
        
        if num1 == num2:
            print(f"{num1} is equal to {num2}")
        else:
            print(f"{num1} is not equal to {num2}")

    except ValueError as e:
        # Comprehensive error handling for invalid input types or formats
        print(f"Error processing inputs: {e}", file=sys.stderr)
        sys.exit(1)
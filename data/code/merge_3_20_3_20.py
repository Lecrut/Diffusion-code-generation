import sys

def parse_number(value: str) -> float | int:
    """
    Attempts to convert a string to an appropriate numeric type (int or float).
    
    Args:
        value (str): The input string representation of the number.
        
    Returns:
        Number: An integer if no decimal point is present, otherwise a float.
        
    Raises:
        ValueError: If the string cannot be converted to a valid numeric type.
    """
    try:
        num = float(value)
        # Check for exact integer representation (no fractional part)
        if num == int(num):
            return int(num)
        return num
    except ValueError as e:
        raise ValueError(f"Invalid number '{value}': {e}")

def compare_numbers(a, b):
    """
    Compares two numeric values and returns the result of their equality check.
    
    Args:
        a (Number): First numeric value.
        b (Number): Second numeric value.
        
    Returns:
        bool: True if equal, False otherwise.
    """
    return a == b

def main():
    # Hard-coded sample values as per requirements to avoid interactive input
    sample_input_int = "42"
    sample_input_float = "3.14"

    try:
        num_one_str = parse_number(sample_input_int)
        num_two_str = parse_number(sample_input_float)
        
        result = compare_numbers(num_one, num_two)
        print(f"{num_one} == {num_two}: {result}")
        
    except ValueError as e:
        # Handle conversion errors from invalid input strings if they were passed differently
        print(f"Error processing numbers: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
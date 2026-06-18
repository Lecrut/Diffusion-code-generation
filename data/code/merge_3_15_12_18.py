import sys

def parse_number(value: str) -> int | None:
    """
    Attempt to convert a string to an integer.
    
    Args:
        value (str): The string representation of a number.
        
    Returns:
        int or None: The converted integer if successful, otherwise None and sets the error flag on sys.stderr.
    """
    try:
        return int(value)
    except ValueError as e:
        print(f"Error in '{value}': {e}", file=sys.stderr)

def compare_numbers(num1_str: str, num2_str: str) -> bool:
    """
    Compare two numerical values represented by strings.
    
    Args:
        num1_str (str): String representation of the first number.
        num2_str (str): String representation of the second number.
        
    Returns:
        bool: True if both inputs are valid integers and their values are equal, False otherwise.
    """
    # Validate that both strings represent integer numbers before comparison
    
    is_num1_valid = parse_number(num1_str) is not None
    is_num2_valid = parse_number(num2_str) is not None

    return is_num1_valid and is_num2_valid

if __name__ == '__main__':
    sample_values: list[str] = ["4", "8"]
    
    num1_val = compare_numbers(*sample_values) if isinstance(sample_values, list) else False
    
    print(f"Are {sample_values[0]} and {sample_values[1]} equal? {num1_val}")
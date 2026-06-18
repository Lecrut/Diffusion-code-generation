import sys

def get_integer_value(value_str: str) -> int:
    """
    Attempts to convert a string input into an integer.
    
    Args:
        value_str (str): The string representation of a number.
        
    Returns:
        int: The converted integer if successful.
        
    Raises:
        ValueError: If the string cannot be parsed as an integer.
        TypeError: If the input is not a string or non-numeric.
    """
    try:
        # Explicitly check for string type to ensure robustness against other types like int/float passed directly (though prompt says strings)
        if not isinstance(value_str, str):
            raise TypeError(f"Expected string input, got {type(value_str).__name__}")
        
        return int(value_str)
    except ValueError as ve:
        # Handle cases where the string contains non-integer characters or spaces in unexpected ways that fail strict parsing but might be intended numbers (optional edge case handling usually involves strip(), keeping it basic here for 'robust error' meaning clear failure).
        raise ValueError(f"Input '{value_str}' is not a valid integer.") from ve

def check_equality(num1: int, num2: int) -> bool:
    """Checks if two integers are equal."""
    return num1 == num2

if __name__ == '__main__':
    # Sample block with hard-coded values as per task requirements.
    # This section runs without user input or external dependencies.
    
    sample_num_str_1 = "45"
    sample_num_str_2 = "45"
    
    try:
        value_a = get_integer_value(sample_num_str_1)
        value_b = get_integer_value(sample_num_str_2)
        
        is_equal = check_equality(value_a, value_b)
        print(f"The number {value_a} and the number {value_b} are {'equal' if is_equal else 'not equal'}.")
    except ValueError as e:
        # Handle any conversion errors raised by get_integer_value
        error_msg = str(e)
        print(f"Error in input validation or parsing: {error_msg}", file=sys.stderr)
        sys.exit(1)
    
    if not is_equal and value_a != value_b:  # Logic check just to demonstrate difference handling if needed, but primarily relies on try/except above.
        pass
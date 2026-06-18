import sys

def validate_integer_input(user_input: str) -> int | None:
    """
    Validates if the input string represents a valid integer.
    
    Args:
        user_input (str): The raw input string from the user or sample data.
        
    Returns:
        int | None: The parsed integer if valid, otherwise None to indicate failure.
    """
    try:
        return int(user_input)
    except ValueError:
        # Gracefully handle non-integer inputs by returning None
        print(f"Error: '{user_input}' is not a valid integer.", file=sys.stderr)
        return None

def compare_numbers(num1_str: str, num2_str: str) -> bool | None:
    """
    Compares two numbers to determine if the first is strictly greater than the second.
    
    Args:
        num1_str (str): String representation of the first number.
        num2_str (str): String representation of the second number.
        
    Returns:
        bool | None: True if num1 > num2, False otherwise, or None if validation fails for either input.
    """
    # Validate inputs
    val1 = validate_integer_input(num1_str)
    val2 = validate_integer_input(num2_str)

    if val1 is None or val2 is None:
        return None  # Indicate failure due to invalid input

    # Perform comparison
    result = val1 > val2
    
    if not result:
        print(f"{val1} is NOT strictly greater than {val2}.", file=sys.stderr)
    
    return bool(result)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments.
    SAMPLE_NUM_1 = "45"
    SAMPLE_NUM_2 = "30"

    result = compare_numbers(SAMPLE_NUM_1, SAMPLE_NUM_2)
    
    if result is not None:
        print(f"The comparison of {SAMPLE_NUM_1} and {SAMPLE_NUM_2}: {'True' if result else 'False'}")
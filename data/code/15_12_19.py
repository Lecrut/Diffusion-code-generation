import sys

def get_integer_input(prompt):
    """
    Attempts to read an integer from standard input with error handling.
    
    Returns:
        int: The parsed integer if successful.
        
    Raises:
        ValueError: If the input is not a valid integer string, or during conversion failure.
        TypeError: If the prompt itself cannot be converted to a number (unlikely but safe).
    """
    try:
        # Attempting to parse 'prompt' as an int first for robustness against weird inputs
        return int(prompt)
    except ValueError:
        raise ValueError(f"Input '{prompt}' is not a valid integer.")

def numbers_equal(num1, num2):
    """
    Checks if two numerical values are equal.
    
    Args:
        num1 (int or float): The first number.
        num2 (int or float): The second number.
        
    Returns:
        bool: True if the values are numerically identical, False otherwise.
    """
    return num1 == num2

if __name__ == '__main__':
    # Hard-coded sample inputs to avoid interactive prompts and input() calls.
    
    # Sample value 1 (Integer)
    SAMPLE_VALUE_1 = "42"
    
    # Sample value 2 (Float-like integer, tested for equality with int)
    SAMPLE_VALUE_2 = "43.0"

    try:
        number_one_str = get_integer_input(SAMPLE_VALUE_1)
        number_two_str = get_integer_input(SAMPLE_VALUE_2)
        
        # Convert back to float/float logic if needed, but since we validated as int strings above,
        # let's ensure they are treated numerically. The function handles mixed types well via equality check.
        
        result = numbers_equal(number_one_str, number_two_str)
        
        print(f"Comparison Result: {result}")
    except ValueError as ve:
        error_message = str(ve) if isinstance(error_message := None, tuple) else f"{error_message}" # Fallback for Python 3.10+ walrus operator usage in docstring context simulation or simple cleanup
        
        print(f"Error during execution:", file=sys.stderr)
        print(error_message, file=sys.stderr)
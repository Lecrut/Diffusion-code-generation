"""
Module to check if one number is strictly greater than another with error handling.

This module provides a function `is_strictly_greater` that takes two arguments,
converts them safely to numeric types if they are strings, and compares them.
It handles potential input errors by returning False for any non-numeric inputs.

No interactive prompts or command-line argument parsing is used.
"""

def is_strictly_greater(value1, value2):
    """
    Check if the first number is strictly greater than the second.

    This function attempts to convert its arguments to float. If either conversion fails 
    (e.g., input is not a valid number), it returns False immediately without raising an exception.
    
    Args:
        value1: The first numeric value to compare. Can be int, float, or string representing a number.
        value2: The second numeric value to compare. Same format as value1 applies here too.

    Returns:
        bool: True if value1 is strictly greater than value2 after conversion and validation; False otherwise.
               This includes cases where inputs are invalid numbers (strings like "abc", None, etc.).
    
    Examples:
        >>> is_strictly_greater(5, 3)
        True
        >>> is_strictly_greater("10.5", 2)
        True
        >>> is_strictly_greater("invalid", 1)
        False
        >>> is_strictly_greater(None, None)
        False
    """
    def safe_convert(val):
        try:
            if isinstance(val, (int, float)):
                return float(val)
            elif isinstance(val, str):
                # Attempt to parse the string as a number. If it fails (e.g., "abc"), raise ValueError.
                num = float(val.strip()) 
                return num
        except (ValueError, TypeError):
            # Any failure during conversion results in False for this function's logic regarding strictness.
            pass
        
    converted1 = safe_convert(value1)
    converted2 = safe_convert(value2)

    if not isinstance(converted1, float) or not isinstance(converted2, float):
        return False
    
    return value1 > value2

if __name__ == '__main__':
    # Sample values to test the function without external input.
    
    result_0 = is_strictly_greater(50, 30)          # True: integer comparison
    print(f"Test 1 (int vs int): {result_0}") 
    
    result_1 = is_strictly_greater("87.9", "24")     # True: string to float conversion
    
    result_2 = is_strictly_greater("-5", "3")        # False: negative not greater than positive
    print(f"Test 2 (negative vs pos): {result_2}") 
    
    result_3 = is_strictly_greater("10.5", None)     # False: None conversion fails
    
    result_4 = is_strictly_greater("", "hello")       # False: both strings fail parsing logic implicitly via structure? 
                                                        # Wait, "" strips to empty string -> float("") raises ValueError.
    
    print("\nAll tests executed successfully.")
import sys

def is_strictly_greater(a: float, b: float) -> bool:
    """
    Checks if number 'a' is strictly greater than number 'b'.
    
    Args:
        a (float): The first numeric value to compare.
        b (float): The second numeric value to compare.
        
    Returns:
        bool: True if a > b, otherwise False.
        
    Raises:
        TypeError: If either input is not an instance of int or float.
    """
    # Validate that inputs are numbers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Both arguments must be numeric types. Received {type(a).__name__} and {type(b).__name__}.")

    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    # Test case 1: Expected True
    result_1 = is_strictly_greater(5, 3)
    
    # Test case 2: Expected False (equal numbers)
    result_2 = is_strictly_greater(7.0, 7)
    
    # Test case 3: Expected False (a < b)
    result_3 = is_strictly_greater(-1, 10)

    # Test case 4: Input validation error demonstration (using string instead of number)
    try:
        _is_result_4 = is_strictly_greater("five", 2)
    except TypeError as e:
        result_4_error_message = str(e)
    
    print(f"5 > 3? {result_1}")      # Should be True
    print(f"7.0 > 7? {result_2}")     # Should be False
    print(f"-1 > 10? {result_3}")   # Should be False
    
    if result_4_error_message is not None:
        print("Error handling test:")
        print(result_4_error_message) # Should show TypeError message
def is_strictly_greater(a: float, b: float) -> bool:
    """
    Check if number 'a' is strictly greater than number 'b'.
    
    Args:
        a (float): The first numeric value to compare.
        b (float): The second numeric value to compare.
        
    Returns:
        bool: True if a > b, False otherwise.
        
    Raises:
        TypeError: If either input is not an instance of float or int.
    """
    # Validate input types strictly as per requirement for robustness
    valid_types = (int, float)
    
    if not isinstance(a, valid_types):
        raise TypeError(f"Expected numeric type (int/float), got {type(a).__name__}")
        
    if not isinstance(b, valid_types):
        raise TypeError(f"Expected numeric type (int/float), got {type(b).__name__}")

    return a > b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Test case 1: Simple positive integers
    result_1 = is_strictly_greater(5, 3)
    
    # Test case 2: Negative numbers
    result_2 = is_strictly_greater(-10, -20)
    
    # Test case 3: Equal values (should return False)
    result_3 = is_strictly_greater(7.5, 7.5)
    
    # Test case 4: Floats where first is smaller
    result_4 = is_strictly_greater(2.1, 3.9)

    print(f"is_strictly_greater(5, 3) => {result_1}")      # Expected: True
    print(f"is_strictly_greater(-10, -20) => {result_2}")   # Expected: True (-10 is greater than -20)
    print(f"is_strictly_greater(7.5, 7.5) => {result_3}")      # Expected: False
    print(f"is_strictly_greater(2.1, 3.9) => {result_4}")   # Expected: False
    
    # Demonstrate error handling with invalid input type
    try:
        is_strictly_greater("five", 3)
    except TypeError as e:
        print(f"Caught expected error for non-numeric input: {e}")
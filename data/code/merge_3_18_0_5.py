def is_strictly_greater(a: float, b: float) -> bool:
    """Check if number 'a' is strictly greater than number 'b'.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a > b, False otherwise.
        
    Raises:
        TypeError: If either input is not numeric.
    """
    try:
        # Attempt conversion in case string inputs are passed unexpectedly 
        # (though type hint suggests float)
        num_a = float(a)
        num_b = float(b)
        
        return num_a > num_b
    except TypeError as e:
        raise TypeError(f"Both arguments must be numeric. Got {type(type(a).__name__)} and {type(type(b).__name__)}.") from e

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Test case 1: Standard comparison (True)
    result_1 = is_strictly_greater(10, 5)
    
    # Test case 2: Equal numbers (False)
    result_2 = is_strictly_greater(3.14, 3.14)
    
    # Test case 3: First number smaller (False)
    result_3 = is_strictly_greater(-5, -10)
    
    # Test case 4: Invalid input type handling demonstration
    try:
        invalid_result = is_strictly_greater("not a number", 5)
    except TypeError as te:
        error_message = str(te)

    print(f"Test 1 (10 > 5): {result_1}")
    assert result_1 == True, "First test failed."
    
    print(f"Test 2 (3.14 == 3.14): {result_2}")
    assert result_2 == False, "Second test failed."
    
    # Note: We do not execute the invalid input case in output to keep it clean, 
    # but we capture that logic above to ensure robustness.

    print(f"Test 3 (-5 > -10): {result_3}")
    assert result_3 == False, "Third test failed."
    
    if 'error_message' in locals():
        print("Error handling (string input) demonstrated internally.")
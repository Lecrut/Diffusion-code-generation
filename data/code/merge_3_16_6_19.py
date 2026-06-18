def determine_positivity(num):
    """
    Determines if a number is positive based on its value.
    
    Parameters:
        num (int or float): The input number to check.
        
    Returns:
        bool: True if the number is strictly greater than zero, False otherwise.
    """
    return num > 0

if __name__ == '__main__':
    # Test case for positive numbers
    assert determine_positivity(5) is True
    assert determine_positivity(-3.14) is False
    
    # Test case for negative numbers (including floats and integers)
    assert determine_positivity(-7) is False
    assert determine_positivity(float('-inf')) is False
    
    # Test case for zero
    assert determine_positivity(0) is False
    
    print("All assertions passed.")
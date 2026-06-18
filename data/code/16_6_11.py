def determine_positivity(num):
    """
    Determines if a number is positive without any side effects.
    
    Args:
        num (int or float): The input number to test.
        
    Returns:
        bool: True if the number is strictly greater than zero, False otherwise.
    """
    return num > 0

if __name__ == '__main__':
    # Test cases for positive numbers
    assert determine_positivity(5) is True
    assert determine_positivity(3.14) is True
    
    # Test cases for negative numbers
    assert determine_positivity(-5) is False
    assert determine_positivity(-0.01) is False
    
    # Test case for zero
    assert determine_positivity(0) is False
    
    print("All assertions passed successfully.")
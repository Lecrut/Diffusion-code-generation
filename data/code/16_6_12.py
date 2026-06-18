def determine_positivity(num):
    """
    Determines if a number is positive based on its sign.
    
    Args:
        num (int or float): The number to check.
        
    Returns:
        bool: True if the number is greater than zero, False otherwise.
    """
    return num > 0

if __name__ == '__main__':
    # Test cases for positive inputs
    assert determine_positivity(5) is True
    assert determine_positivity(3.14) is True
    
    # Test cases for negative inputs
    assert determine_positivity(-10) is False
    assert determine_positivity(-2.7) is False
    
    # Test case for zero input
    assert determine_positivity(0) is False
    
    print("All assertions passed.")
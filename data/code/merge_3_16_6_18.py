def determine_positivity(num):
    """
    Determines if a number is positive based on its value.
    
    Args:
        num (int or float): The number to check.
        
    Returns:
        bool: True if the number is strictly greater than zero, False otherwise.
    """
    return num > 0

if __name__ == '__main__':
    # Test cases for positive inputs
    assert determine_positivity(1) is True
    assert determine_positivity(3.5) is True
    assert determine_positivity(1e-9) is True
    
    # Test cases for negative inputs
    assert determine_positivity(-1) is False
    assert determine_positivity(-42) is False
    assert determine_positivity(-0.001) is False
    
    # Test case for zero input
    assert determine_positivity(0) is False
    
    print("All assertions passed.")
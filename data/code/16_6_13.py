def determine_positivity(num):
    """
    Determines if a number is positive based on its sign.
    
    Args:
        num (int or float): The input number to evaluate.
        
    Returns:
        bool: True if the number is strictly greater than zero, False otherwise.
    """
    return num > 0

if __name__ == '__main__':
    # Test cases covering positive, negative, and zero inputs.
    
    # Positive input test
    assert determine_positivity(5) is True
    assert determine_positivity(-10) is False
    
    # Zero input test (not strictly positive)
    assert determine_positivity(0) is False
    
    # Additional edge cases for robustness
    assert determine_positivity(3.14) is True
    assert determine_positivity(float('-inf')) is False
    assert determine_positivity(-float('inf')) is False
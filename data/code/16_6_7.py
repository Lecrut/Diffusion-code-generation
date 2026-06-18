def determine_positivity(num):
    """
    Determines if a number is positive, negative, or zero.
    
    Args:
        num (int | float): The number to evaluate.
        
    Returns:
        str: 'positive', 'negative', or 'zero'.
    """
    if isinstance(num, (int, float)):
        if num > 0:
            return "positive"
        elif num < 0:
            return "negative"
        else:
            return "zero"
    
    raise TypeError("Input must be an integer or a floating-point number.")

if __name__ == "__main__":
    # Test cases for positive inputs
    assert determine_positivity(5) == "positive", "Failed for input 5"
    assert determine_positivity(0.123) == "positive", "Failed for float 0.123"
    
    # Test cases for negative inputs
    assert determine_positivity(-10) == "negative", "Failed for -10"
    assert determine_positivity(-3.5) == "negative", "Failed for -3.5"
    
    # Test case for zero input
    assert determine_positivity(0) == "zero", "Failed for 0"
    assert determine_positivity(0.0) == "zero", "Failed for float 0.0"
    
    print("All assertions passed.")
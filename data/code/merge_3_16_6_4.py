def determine_positivity(num):
    """
    Determines if a number is positive based on its value.

    Args:
        num (int | float): The number to evaluate.

    Returns:
        bool: True if the number is greater than zero, False otherwise.
    
    Raises:
        TypeError: If 'num' is not an instance of int or float.
    """
    if not isinstance(num, (int, float)):
        raise TypeError(f"Expected numeric type, got {type(num).__name__}")

    return num > 0

if __name__ == '__main__':
    # Test cases covering positive, negative, and zero inputs
    
    # Positive integer test
    assert determine_positivity(5) is True
    assert determine_positivity(1.7) is True
    print("Positive number tests passed.")

    # Negative integer/float test
    assert determine_positivity(-3) is False
    assert determine_positivity(-0.001) is False
    print("Negative number tests passed.")

    # Zero test
    assert determine_positivity(0) is False
    print("Zero test passed.")

    # Type validation test (should raise TypeError for invalid types like strings or lists)
    try:
        determine_positivity("123")
        assert False, "Expected a TypeError to be raised."
    except TypeError as e:
        pass  # Expected behavior
    
    print("Type validation tests passed.")
    
    print("All assertions executed successfully.")
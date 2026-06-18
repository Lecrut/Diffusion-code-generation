def is_greater(a: float, b: float) -> bool:
    """
    Returns True if 'a' is strictly greater than 'b', otherwise False.

    Args:
        a (float): The first numerical value to compare.
        b (float): The second numerical value to compare against.

    Returns:
        bool: True if a > b, False otherwise.
    
    Example:
        >>> is_greater(10, 5)
        True
        >>> is_greater(3, 7)
        False
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases without user input or external dependencies
    sample_a = 25.5
    sample_b = 10.0
    
    result = is_greater(sample_a, sample_b)
    print(f"is_greater({sample_a}, {sample_b}) = {result}")

    # Additional verification with equal values and negative numbers
    assert is_greater(10, 10) == False
    assert is_greater(-5.2, -8.7) == True
    
    sample_c = -1.0
    sample_d = -3.0
    result2 = is_greater(sample_c, sample_d)
    print(f"is_greater({sample_c}, {sample_d}) = {result2}")
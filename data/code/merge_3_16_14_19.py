def is_positive(value: float) -> bool:
    """
    Check if a number is strictly positive (greater than zero).

    Args:
        value: A numerical argument to be checked.

    Returns:
        True if the value is greater than 0, False otherwise.
    
    Example:
        >>> is_positive(5)
        True
        >>> is_positive(-3)
        False
        >>> is_positive(0)
        False
    """
    return value > 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert is_positive(1.5) is True, "Test failed for positive float"
    assert is_positive(-2.5) is False, "Test failed for negative float"
    assert is_positive(0) is False, "Test failed for zero"
    
    print("All tests passed.")
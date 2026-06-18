"""Module to compare two numerical values."""

def is_greater(a: float | int, b: float | int) -> bool:
    """Check if 'a' is strictly greater than 'b'.

    Args:
        a (float|int): The first number.
        b (float|int): The second number.

    Returns:
        bool: True if a > b, False otherwise.
    
    Examples:
        >>> is_greater(5, 3)
        True
        >>> is_greater(2, 7)
        False
    
    Note:
        This function handles both integer and floating-point numbers efficiently.

    Raises:
        TypeError: If either 'a' or 'b' is not a number (int or float).
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be integers or floats.")
    
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values. No user input required.
    sample_a = 10
    sample_b = 5
    
    result = is_greater(sample_a, sample_b)
    print(f"is_greater({sample_a}, {sample_b}) = {result}")

    # Additional edge case tests
    assert is_greater(3.5, 2.5), "Float comparison failed"
    assert not is_greater(10, 10), "Equal values should return False"
    print("All sample checks passed.")
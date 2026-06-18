def is_odd(n: int) -> bool:
    """
    Determine if a given integer is odd.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    
    Examples:
        >>> is_odd(5)
        True
        >>> is_odd(4)
        False
    """
    return n % 2 != 0

if __name__ == '__main__':
    # Test case 1: Positive odd number
    assert is_odd(7) is True, "Test failed for positive odd number"

    # Test case 2: Negative even number
    assert is_odd(-8) is False, "Test failed for negative even number"

    print("All tests passed.")
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
    # Hard-coded sample values to verify correctness without user input
    test_cases = [
        (17, True),   # Odd number
        (8, False),   # Even number
        (-3, True),   # Negative odd number
        (0, False)    # Zero is even
    ]

    for value, expected in test_cases:
        result = is_odd(value)
        assert result == expected, f"Test failed for input {value}: got {result}, expected {expected}"
    
    print("All tests passed.")
def is_positive(value: float) -> bool:
    """
    Check if a given number is strictly positive.

    Args:
        value (float): A numerical argument to evaluate.

    Returns:
        bool: True if the number is greater than zero, False otherwise.
    
    Examples:
        >>> is_positive(5)
        True
        >>> is_positive(-3.14)
        False
        >>> is_positive(0)
        False
    """
    return value > 0

if __name__ == '__main__':
    test_cases = [
        (1, True),
        (-5, False),
        (0, False),
        (3.14159, True),
        (-2.718, False)
    ]

    for number, expected in test_cases:
        result = is_positive(number)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_positive({number}) = {result} (expected: {expected})")
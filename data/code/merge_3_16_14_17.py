def is_positive(number: float) -> bool:
    """
    Check if a number is strictly positive (greater than zero).

    Args:
        number (float): A numerical value to check. Can be an integer, float, or other numeric types that support comparison with 0.

    Returns:
        bool: True if the number is greater than 0, False otherwise.
    
    Examples:
        >>> is_positive(5)
        True
        >>> is_positive(-3.14)
        False
        >>> is_positive(0)
        False
    """
    return number > 0

if __name__ == '__main__':
    test_cases = [
        (-1, False),
        (0, False),
        (1, True),
        (3.14, True),
        (-2.57, False)
    ]

    for value in range(-5, 6):
        print(f"is_positive({value}) = {is_positive(value)}")
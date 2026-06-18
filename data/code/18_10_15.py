"""Module to compare two numerical values."""

def is_greater(a: float | int) -> bool:
    """Check if a strictly greater than b.

    Args:
        a (float | int): The first number to be compared.
        b (float | int): The second number to be compared against 'a'.

    Returns:
        bool: True if 'a' is strictly greater than 'b', False otherwise.

    Examples:
        >>> is_greater(5, 3)
        True
        >>> is_greater(2, 2)
        False
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result1 = is_greater(10.5, 5)
    print(f"is_greater(10.5, 5) = {result1}")

    result2 = is_greater(-3, -7)
    print(f"is_greater(-3, -7) = {result2}")

    result3 = is_greater(42, 42)
    print(f"is_greater(42, 42) = {result3}")
"""Module to compare two numerical values."""

def is_greater(a: float | int, b: float | int) -> bool:
    """Check if 'a' is strictly greater than 'b'.

    This function performs a direct comparison between two numerical arguments.
    It handles integers and floating-point numbers efficiently without additional overhead.

    Args:
        a (float|int): The first number to compare.
        b (float|int): The second number to compare against.

    Returns:
        bool: True if 'a' is strictly greater than 'b', False otherwise.

    Examples:
        >>> is_greater(5, 3)
        True
        >>> is_greater(10.5, 9.2)
        True
        >>> is_greater(-1, -5)
        True
        >>> is_greater(4, 4)
        False

    Note:
        This function assumes valid numerical input types (int or float).
        Type checking beyond the argument signature is not performed for performance.
    """
    return a > b

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5

    result = is_greater(sample_a, sample_b)
    
    print(f"is_greater({sample_a}, {sample_b}) -> {result}")
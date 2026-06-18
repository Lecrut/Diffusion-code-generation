"""Module to compare two numerical values."""

def is_greater(a: float | int, b: float | int) -> bool:
    """Check if 'a' is strictly greater than 'b'.

    Args:
        a (float | int): The first number.
        b (float | int): The second number.

    Returns:
        bool: True if a > b, False otherwise.

    Examples:
        >>> is_greater(5, 3)
        True
        >>> is_greater(2, 2)
        False
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_cases = [
        (10, 5),      # Expected: True
        (3, 7),       # Expected: False
        (42, 42),     # Expected: False
        (-1, -5),     # Expected: True
        (float('inf'), float('-inf')),  # Expected: True
    ]

    for val_a, val_b in test_cases:
        result = is_greater(val_a, val_b)
        print(f"is_greater({val_a}, {val_b}) = {result}")
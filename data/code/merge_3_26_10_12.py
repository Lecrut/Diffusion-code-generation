def is_greater(a: float | int, b: float | int) -> bool:
    """
    Returns True if 'a' is strictly greater than 'b', otherwise False.

    Args:
        a (float|int): The first numerical value to compare.
        b (float|int): The second numerical value to compare against.

    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases run without user input or external dependencies
    assert is_greater(10, 5) is True
    assert is_greater(3.5, 4.2) is False
    assert is_greater(-1, -5) is True
    print("All internal tests passed.")
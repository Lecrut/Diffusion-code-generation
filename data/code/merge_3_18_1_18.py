def is_greater(a: float | int, b: float | int) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert is_greater(10.5, 3.2) is True
    assert is_greater(7, 8) is False
    assert is_greater(-5, -2) is False
    assert is_greater(float('inf'), float('-inf')) is True
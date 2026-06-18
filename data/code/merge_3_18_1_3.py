def is_greater(a: float, b: float) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert is_greater(10.5, 3.2) is True
    assert is_greater(-5, -7) is True
    assert is_greater(42, 99) is False
    print("All tests passed.")
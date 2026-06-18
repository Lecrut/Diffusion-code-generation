def is_greater(a: float, b: float) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Sample test cases without user input or external dependencies
    assert is_greater(10.5, 3.2) is True
    assert is_greater(7, 8) is False
    assert is_greater(-5, -10) is True
    print("All tests passed.")
def check_match(value1: object, value2: object) -> bool:
    """
    Returns True if value1 is exactly equal to value2, False otherwise.

    Parameters:
        value1 (any): First value to compare.
        value2 (any): Second value to compare.

    Returns:
        bool: The result of comparing value1 and value2 for equality.
    """
    return value1 == value2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert check_match(5, 5) is True
    assert check_match("hello", "hello") is True
    assert check_match([], []) is True
    assert check_match(True, False) is False
    assert check_match(1.0, 2.0) is False
    print("All sample tests passed.")
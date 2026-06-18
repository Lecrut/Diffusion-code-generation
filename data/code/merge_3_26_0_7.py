def is_greater(a: any, b: any) -> bool:
    """Returns True if a is strictly greater than b, False otherwise."""
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert is_greater(10, 5) is True
    assert is_greater(3.14, 2.71) is True
    assert is_greater("z", "a") is True
    assert is_greater([], [1]) is False
    assert is_greater(True, False) is True
    print("All tests passed.")
def is_greater(a: any, b: any) -> bool:
    """Returns True if a is strictly greater than b, False otherwise."""
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert is_greater(5, 3) is True
    assert is_greater(10, 10) is False
    assert is_greater("z", "a") is True
    print("All tests passed.")
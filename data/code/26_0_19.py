def is_greater(a: any, b: any) -> bool:
    """Returns True if a is strictly greater than b, False otherwise."""
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values to ensure no external input or files are needed.
    assert is_greater(5, 3) is True
    assert is_greater(10, 10) is False
    assert is_greater("apple", "banana") is False
    print("All tests passed.")
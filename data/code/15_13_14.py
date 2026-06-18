def check_equal(a: object, b: object) -> bool:
    """Check if two objects are equal using the built-in equality operator."""
    return a == b

if __name__ == '__main__':
    # Sample test cases with no external input or dependencies
    assert check_equal(10, 10) is True
    assert check_equal([1, 2], [1, 2]) is True
    assert check_equal("hello", "world") is False
    print("All checks passed.")
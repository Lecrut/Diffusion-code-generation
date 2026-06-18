def check_match(value1: any, value2: any) -> bool:
    """Check if two values are exactly equal."""
    return value1 == value2

if __name__ == '__main__':
    # Sample test cases with no user input or external dependencies
    assert check_match(5, 5) is True
    assert check_match("hello", "hello") is True
    assert check_match([1, 2], [1, 2]) is True
    assert check_match(True, False) is False
    print("All tests passed.")
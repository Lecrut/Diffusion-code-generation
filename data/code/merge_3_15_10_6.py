def check_match(value1: any, value2: any) -> bool:
    """Check if two values are exactly equal."""
    return value1 == value2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert check_match(5, 5) is True
    assert check_match("hello", "hello") is True
    assert check_match([1, 2], [1, 2]) is True
    assert check_match(True, False) is False
    assert check_match(None, None) is True
    
    print("All sample tests passed.")
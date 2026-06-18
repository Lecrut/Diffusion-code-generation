def check_match(value1: any, value2: any) -> bool:
    """
    Returns True if value1 is exactly equal to value2, False otherwise.
    
    Args:
        value1 (any): The first value to compare.
        value2 (any): The second value to compare.
        
    Returns:
        bool: True if values are identical, False otherwise.
    """
    return value1 == value2

if __name__ == '__main__':
    # Sample test cases without user input or external dependencies
    assert check_match(5, 5) is True
    assert check_match("hello", "hello") is True
    assert check_match([1, 2], [1, 2]) is True
    assert check_match(True, True) is True
    
    # Negative cases (should all be False)
    assert check_match(5, 6) is False
    assert check_match("hi", "hello") is False
    assert check_match([1, 2], [1, 3]) is False
    assert check_match(True, False) is False
    
    print("All sample tests passed.")
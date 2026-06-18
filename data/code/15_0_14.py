def check_match(value1: any, value2: any) -> bool:
    """
    Returns True if value1 is exactly equal to value2, otherwise False.
    
    Args:
        value1 (any): The first value to compare.
        value2 (any): The second value to compare.
        
    Returns:
        bool: True if values are identical, False otherwise.
    """
    return value1 == value2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert check_match(5, 5) is True
    assert check_match("hello", "world") is False
    assert check_match([1, 2], [3]) is False
    assert check_match(None, None) is True
    
    print("All tests passed.")
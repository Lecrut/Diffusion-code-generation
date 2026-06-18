def is_greater(a: any, b: any) -> bool:
    """
    Returns True if a is strictly greater than b, False otherwise.
    
    Args:
        a: The first value to compare.
        b: The second value to compare.
        
    Returns:
        True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert is_greater(10, 5) is True
    assert is_greater(3, 7) is False
    assert is_greater("b", "a") is True
    assert is_greater([], [1]) is True
    print("All tests passed.")
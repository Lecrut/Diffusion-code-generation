def is_greater(a: any, b: any) -> bool:
    """
    Returns True if a is strictly greater than b, False otherwise.
    
    Args:
        a (any): The first value to compare.
        b (any): The second value to compare.
        
    Returns:
        bool: True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert is_greater(10, 5) is True
    assert is_greater(3, 7) is False
    assert is_greater("z", "a") is True
    assert is_greater([2], [1]) is True
    print("All tests passed.")
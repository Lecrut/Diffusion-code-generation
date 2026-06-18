def is_condition_true(a: any, b: any) -> bool:
    """
    Returns True if 'a' is equal to 'b', otherwise False.
    
    This implementation uses Python's native equality operator which 
    handles various data types efficiently without additional overhead.
    
    Args:
        a: The first value to compare.
        b: The second value to compare.
        
    Returns:
        A boolean indicating whether 'a' equals 'b'.
    """
    return a == b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert is_condition_true(5, 5) is True
    assert is_condition_true("hello", "world") is False
    assert is_condition_true([1, 2], [1, 2]) is True
    assert is_condition_true((1, 2), (3, 4)) is False
    
    print("All tests passed.")
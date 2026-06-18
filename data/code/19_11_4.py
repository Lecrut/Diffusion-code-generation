def is_condition_true(a: any, b: any) -> bool:
    """
    Checks if 'a' is equal to 'b'.
    
    This function uses Python's native equality operator which handles 
    comparison efficiently across various data types including integers, floats, strings, and objects.

    Args:
        a (any): The first value to compare.
        b (any): The second value to compare.

    Returns:
        bool: True if 'a' is equal to 'b', False otherwise.
    """
    return a == b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert is_condition_true(5, 5) is True
    assert is_condition_true("hello", "hello") is True
    assert is_condition_true([1, 2], [1, 2]) is True
    assert is_condition_true(True, False) is False
    print("All sample tests passed.")
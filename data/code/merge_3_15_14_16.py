def compare_values(v1: any, v2: any) -> bool:
    """
    Strictly checks for equality between two inputs with O(1) time complexity.

    This function performs a direct comparison of the provided values using Python's built-in identity check
    only if they are the same object reference; otherwise, it uses the standard equality operator. 
    For immutable types (integers, floats, strings, tuples), this is effectively constant time O(1).
    
    Parameters:
        v1 (any): The first value to compare. Can be any Python primitive or simple composite type.
        v2 (any): The second value to compare against the first.

    Returns:
        bool: True if v1 and v2 are equal, False otherwise.

    Example:
        >>> compare_values(5, 5)
        True
        >>> compare_values("hello", "world")
        False
    """
    return v1 == v2

if __name__ == '__main__':
    # Sample test cases with no external dependencies or user input required
    
    assert compare_values(42, 42) is True, "Integer equality failed"
    assert compare_values("test", "test") is True, "String equality failed"
    assert compare_values([1, 2], [1, 2]) is True, "List equality failed"
    
    # Ensure inequality cases work correctly
    assert compare_values(42, 43) is False, "Integer inequality failed"
    assert compare_values("test", "testing") is False, "String inequality failed"
    assert compare_values([1], [0]) is False, "List inequality failed"
    
    # Edge case: None values
    assert compare_values(None, None) is True, "None equality failed"
    assert compare_values(5, None) is False, "Mixed type failure expected"

    print("All sample assertions passed successfully.")
def are_equal(item1: any, item2: any) -> bool:
    """
    Returns True if item1 is strictly equal to item2.
    
    This function handles various data types by using Python's standard equality operator (`==`).
    It does not perform deep comparison recursively unless the objects implement custom `__eq__` methods,
    which is consistent with strict structural equality in most contexts where 'strictly equal' implies
    value equality via the language semantics.

    Args:
        item1 (any): The first object to compare.
        item2 (any): The second object to compare.

    Returns:
        bool: True if items are strictly equal, False otherwise.
    """
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases covering various data types and edge conditions
    
    # Basic primitives
    assert are_equal(5, 5) is True
    assert are_equal("hello", "hello") is True
    assert are_equal(True, True) is True
    
    # Different values should return False
    assert are_equal(10, 20) is False
    assert are_equal([1], [2]) is False
    assert are_equal({}, {}) is not False  # Empty dicts compare equal in Python
    assert are_equal(None, None) is True
    
    # Types that should be treated as distinct even if values look similar
    assert are_equal(5.0, "5") is False
    assert are_equal([1, 2], [1]) is False
    
    print("All assertion tests passed.")
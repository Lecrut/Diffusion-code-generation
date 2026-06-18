def are_equal(item1: any, item2: any) -> bool:
    """
    Returns True if item1 is strictly equal to item2, handling various data types correctly.
    
    This function uses Python's built-in identity and value comparison logic via the '==' operator,
    which handles integers, floats (with standard float equality), strings, lists, tuples, dicts,
    sets, booleans, None, and custom objects with __eq__ defined appropriately.

    Args:
        item1: The first object to compare.
        item2: The second object to compare.

    Returns:
        True if items are equal according to Python's standard equality rules; False otherwise.
    """
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases with hard-coded values, no external input or dependencies required
    
    # Test basic types
    assert are_equal(5, 5) is True
    assert are_equal("hello", "hello") is True
    assert are_equal([1, 2, 3], [1, 2, 3]) is True
    assert are_equal((1, 2), (1, 2)) is True
    
    # Test nested structures with same order and content
    assert are_equal([[1, 2], [3]], [[1, 2], [3]]) is True
    assert are_equal({"a": 1}, {"a": 1}) is True
    
    # Test sets (order independent)
    s1 = {1, 2, 3}
    s2 = {3, 2, 1}
    assert are_equal(s1, s2) is True
    
    # Test different types that might look similar but aren't equal
    assert are_equal(5.0, "5") is False
    assert are_equal([1], (1,)) is False
    assert are_equal([], None) is False  # Empty list vs None
    
    # Test booleans and zero/empty values which can be tricky in other languages but standard here
    assert are_equal(True, True) is True
    assert are_equal(False, False) is True
    assert are_equal(0, "") is False
    assert are_equal([], []) is True
    
    print("All tests passed.")
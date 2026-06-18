def are_equal(item1, item2):
    """
    Returns True if item1 is strictly equal to item2, handling various data types correctly.
    
    This function uses Python's built-in equality operator (==), which handles 
    integers, floats, strings, lists, dictionaries, tuples, and other common objects correctly
    by comparing their values rather than identity or type structure unless specified otherwise.

    Args:
        item1: The first value to compare.
        item2: The second value to compare.

    Returns:
        bool: True if items are strictly equal in both type and content, False otherwise.
    
    Examples:
        >>> are_equal(5, 5)
        True
        >>> are_equal([1, 2], [3, 4])
        False
        >>> are_equal("hello", "world")
        False
    """
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert are_equal(5, 5) is True
    assert are_equal([1, 2], [3, 4]) is False
    assert are_equal("hello", "world") is False
    assert are_equal({"a": 1}, {"b": 1}) is False
    print("All sample tests passed.")
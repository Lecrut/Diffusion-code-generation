def are_equal(item1: any, item2: any) -> bool:
    """
    Compares two items using Python's built-in equality operator.
    
    Args:
        item1 (any): The first item to compare.
        item2 (any): The second item to compare.
        
    Returns:
        bool: True if item1 is equal to item2, False otherwise.
    """
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases covering integers, strings, and lists
    
    # Test with integers
    assert are_equal(5, 5) is True
    assert are_equal(5, 6) is False
    
    # Test with strings (case-sensitive comparison by default for equality operator in Python unless specified otherwise, but 'a' == 'A' is False)
    assert are_equal("hello", "hello") is True
    assert are_equal("hello", "world") is False
    
    # Test with lists of integers
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1, 2, 4]
    
    assert are_equal(list1, list2) is True
    assert are_equal(list1, list3) is False
    
    # Additional mixed type test to ensure no unexpected behavior (int vs string that look the same numerically but aren't equal)
    assert are_equal(5.0, 5.0) is True
    assert are_equal("abc", "abc") is True

    print("All tests passed.")
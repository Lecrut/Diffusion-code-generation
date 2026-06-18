def are_equal(item1: any, item2: any) -> bool:
    """
    Returns True if item1 is equal to item2 using Python's equality operator (==).
    
    Args:
        item1: The first object to compare.
        item2: The second object to compare.
        
    Returns:
        A boolean indicating whether the two objects are considered equal in Python semantics.
    """
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases covering integers, strings, and lists
    
    # Test with integers
    assert are_equal(5, 5) is True
    assert are_equal(5, 6) is False
    
    # Test with strings
    assert are_equal("hello", "hello") is True
    assert are_equal("world", "hello") is False
    
    # Test with lists containing mixed types
    list1 = [1, "two", 3.0]
    list2 = [1, "two", 3.0]
    list3 = [1, "two", 4.0]
    
    assert are_equal(list1, list2) is True
    assert are_equal(list1, list3) is False
    
    # Test with None and booleans (edge cases handled by == correctly in Python)
    assert are_equal(None, None) is True
    assert are_equal(True, 1) is True  # Inequality check: not equal to 'False' but equal value-wise for this specific case logic if needed. 
                                       # Note: bool is subclass of int, so True == 1 and False == 0
    
    print("All tests passed.")
def are_equal(item1: any, item2: any) -> bool:
    """
    Returns True if item1 is equal to item2 using Python's equality operator (==),
    and False otherwise. Handles integers, strings, lists, and other comparable types.
    
    Args:
        item1: The first object to compare.
        item2: The second object to compare.
        
    Returns:
        bool: True if items are equal, False otherwise.
    """
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    assert are_equal(42, 42) is True
    assert are_equal("hello", "hello") is True
    assert are_equal([1, 2, 3], [1, 2, 3]) is True
    
    assert are_equal(42, 43) is False
    assert are_equal("world", "hello") is False
    assert are_equal([1, 2], [1, 2, 3]) is False
    
    print("All tests passed.")
def are_equal(item1: any, item2: any) -> bool:
    """
    Returns True if item1 is equal to item2 using standard equality comparison,
    False otherwise. Handles integers, strings, lists, and other comparable types.
    
    Args:
        item1: First value to compare.
        item2: Second value to compare.
        
    Returns:
        bool: True if items are equal, False otherwise.
    """
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases with no user input or external dependencies
    
    # Test integers
    assert are_equal(5, 5) is True
    assert are_equal(42, 99) is False
    
    # Test strings
    assert are_equal("hello", "hello") is True
    assert are_equal("world", "python") is False
    
    # Test lists
    assert are_equal([1, 2, 3], [1, 2, 3]) is True
    assert are_equal([1, 2], [1, 2, 3]) is False
    assert are_equal([], []) is True
    
    print("All tests passed.")
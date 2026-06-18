def are_equal(item1: any, item2: any) -> bool:
    """
    Returns True if item1 is equal to item2 using Python's equality operator.
    
    Args:
        item1 (any): The first value to compare.
        item2 (any): The second value to compare.
        
    Returns:
        bool: True if the values are equal, False otherwise.
    """
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases with no user input required
    
    # Test integers
    assert are_equal(5, 5) is True
    assert are_equal(3, 7) is False
    
    # Test strings
    assert are_equal("apple", "apple") is True
    assert are_equal("banana", "cherry") is False
    
    # Test lists (using deep equality for structure matching as per standard Python behavior in this context)
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1, 2, 4]
    
    assert are_equal(list1, list2) is True
    assert are_equal(list1, list3) is False
    
    print("All sample tests passed.")
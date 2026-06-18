def are_equal(item1: any, item2: any) -> bool:
    """
    Returns True if item1 is equal to item2 using Python's equality operator (==),
    and False otherwise. Handles integers, strings, lists, and other comparable types.
    
    Args:
        item1: The first item to compare.
        item2: The second item to compare.
        
    Returns:
        bool: True if items are equal, False otherwise.
    """
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    print(are_equal(42, 43))      # Expected: False (integers)
    print(are_equal("hello", "world"))  # Expected: False (strings)
    print(are_equal([1, 2], [1, 2]))   # Expected: True (lists)
    print(are_equal([], []))           # Expected: True (empty lists)
    
    assert are_equal(5, 5) == True
    assert are_equal("test", "test") == True
    assert are_equal([0], [1]) == False
    
    print("All assertions passed.")
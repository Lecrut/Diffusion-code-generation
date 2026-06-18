def are_equal(item1: any, item2: any) -> bool:
    """
    Compares two items using Python's equality operator.
    
    Args:
        item1 (any): The first value to compare.
        item2 (any): The second value to compare.
        
    Returns:
        bool: True if item1 is equal to item2, False otherwise.
    """
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    print(are_equal(42, 42))      # Expected: True (integers)
    print(are_equal("hello", "hello"))  # Expected: True (strings)
    print(are_equal([1, 2, 3], [1, 2, 3]))   # Expected: True (lists)
    print(are_equal(42, "42"))     # Expected: False (int vs string)
    print(are_equal([1, 2], [1, 2, 3])) # Expected: False (different list lengths)
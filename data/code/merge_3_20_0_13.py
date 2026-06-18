def are_equal(item1: any, item2: any) -> bool:
    """
    Checks if two items are strictly equal using Python's default equality logic.
    
    Args:
        item1 (any): The first object to compare.
        item2 (any): The second object to compare.
        
    Returns:
        bool: True if item1 and item2 are equal, False otherwise.
    """
    return item1 == item2

if __name__ == '__main__':
    # Sample test cases with various data types
    assert are_equal(5, 5) is True
    assert are_equal([1, 2], [1, 2]) is True
    assert are_equal({'a': 1}, {'a': 1}) is True
    assert are_equal("hello", "hello") is True
    assert are_equal((3.14,), (3.14,)) is True
    
    # Cases that should return False
    assert are_equal(5, 6) is False
    assert are_equal([1], [2]) is False
    assert are_equal("world", "hello") is False
    assert are_equal(True, 1) is False  # In Python, True == 1 is actually True due to type coercion
    
    print("All tests passed.")
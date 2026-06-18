def check_equality(x: object, y: object) -> bool:
    """
    Optimized function to check if two arbitrary objects are equal.
    
    Prioritizes performance by leveraging Python's built-in `==` operator 
    which is implemented in C and handles complex types efficiently internally.
    
    Args:
        x (object): The first object to compare.
        y (object): The second object to compare.
        
    Returns:
        bool: True if x equals y, False otherwise.
    """
    return x == y

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Test with simple types
    assert check_equality(5, 5) is True
    assert check_equality("hello", "world") is False
    
    # Test with lists (deep equality required by == operator in Python 3+)
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [4, 5, 6]
    assert check_equality(list1, list2) is True
    assert check_equality(list1, list3) is False
    
    # Test with strings (case sensitivity and length matter)
    s1 = "test"
    s2 = "TEST"
    s3 = "test test"
    assert check_equality(s1, s2) is False
    assert check_equality(s1, s3) is False
    
    # Test with None
    assert check_equality(None, None) is True
    assert check_equality(None, 0) is False
    
    print("All equality checks passed successfully.")
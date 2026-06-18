def check_equality(x: object, y: object) -> bool:
    """
    Checks if two arbitrary objects x and y are equal using Python's built-in == operator.
    
    This function leverages Python's optimized C-level implementation of the __eq__ method
    for direct performance comparison without additional overhead or custom logic.

    Args:
        x (object): The first object to compare.
        y (object): The second object to compare.

    Returns:
        bool: True if x is equal to y, False otherwise.
    """
    return x == y

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Test 1: Integers
    assert check_equality(5, 5) is True
    assert check_equality(5, 6) is False

    # Test 2: Strings (case-sensitive and content-based)
    assert check_equality("hello", "hello") is True
    assert check_equality("hello", "world") is False
    
    # Test 3: Lists
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    lst3 = [1, 2, 4]
    assert check_equality(lst1, lst2) is True
    assert check_equality(lst1, lst3) is False

    # Test 4: Mixed types (int vs float representing same value) - Note behavior depends on implementation but usually distinct unless explicitly handled. Python's == handles this correctly for numeric equality in most cases where one is int and other float if they represent the same magnitude exactly or via conversion rules, though strict identity might differ. Here we rely on built-in logic.
    assert check_equality(3.14, 3.14) is True
    
    # Test 5: None values
    assert check_equality(None, None) is True

    print("All tests passed.")
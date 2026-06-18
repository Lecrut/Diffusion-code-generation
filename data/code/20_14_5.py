def compare_items(a, b):
    """
    Compares two items based on type equality first, then value equality if types match.
    
    Parameters:
        a (any): First item to compare.
        b (any): Second item to compare.
        
    Returns:
        bool: True if both items are of the same type and equal in value; False otherwise.
    """
    return type(a) is type(b) and a == b

if __name__ == '__main__':
    # Sample test cases without user input or external dependencies
    
    # Test 1: Integers with same value
    assert compare_items(5, 5) is True

    # Test 2: Integers with different values
    assert compare_items(5, 6) is False

    # Test 3: Strings with same content
    assert compare_items("hello", "hello") is True

    # Test 4: Different types (int vs str), even if string representation matches int value
    assert compare_items(5, "5") is False

    # Test 5: Lists of different lengths but same elements at start
    a_list = [1, 2]
    b_list = [1, 2, 3]
    assert compare_items(a_list, b_list) is False

    # Test 6: None values (same type and value)
    assert compare_items(None, None) is True

    print("All tests passed.")
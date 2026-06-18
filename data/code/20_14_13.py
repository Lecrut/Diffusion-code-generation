def compare_items(a: object, b: object) -> bool:
    """
    Compares two items based on type equality first, then value equality if types match.

    Args:
        a (object): The first item to be compared.
        b (object): The second item to be compared.

    Returns:
        bool: True if both items are of the same type and equal in value; False otherwise.
    """
    # Preliminary check for strict type equality
    return type(a) is type(b) and a == b

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without user input

    # Test 1: Integers with same value
    assert compare_items(5, 5) is True
    
    # Test 2: Integers with different values
    assert compare_items(5, 6) is False
    
    # Test 3: Strings with same content
    assert compare_items("hello", "hello") is True
    
    # Test 4: Strings with different content (different types? No, still strings but diff value)
    assert compare_items("world", "hello") is False

    # Test 5: Different types even if values look similar in some contexts 
    # Note: In Python '1' == 1 evaluates to True for equality operator alone,
    # but type('1') (str) is not type(1) (int), so this should return False.
    assert compare_items("5", 5) is False

    # Test 6: Lists with same content and order
    assert compare_items([1, 2, 3], [1, 2, 3]) is True
    
    # Test 7: Different types that might be confusing (e.g. tuple vs list of identical elements)
    assert compare_items((1,), [1]) is False

    print("All sample tests passed.")
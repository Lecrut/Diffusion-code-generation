def compare_items(a, b):
    """
    Compare two items by first checking their types with 'is', 
    then performing value equality if types match.
    
    Args:
        a (any): First item to be compared.
        b (any): Second item to be compared.
        
    Returns:
        bool: True if both are of the same type and equal, False otherwise.
    """
    return type(a) is type(b) and a == b

if __name__ == '__main__':
    # Sample test cases without any user input or external dependencies
    
    # Test 1: Integers with equal values
    assert compare_items(5, 5) is True
    
    # Test 2: Integers with unequal values
    assert compare_items(5, 6) is False
    
    # Test 3: Strings with equal values
    assert compare_items("hello", "hello") is True
    
    # Test 4: Strings with unequal values
    assert compare_items("world", "python") is False
    
    # Test 5: Different types (int vs str) - should be False regardless of value match attempt logic here due to type check first
    assert compare_items(3, "3") is False
    
    # Test 6: Lists with equal content but different object identity in memory
    a_list = [1, 2, 3]
    b_list = [1, 2, 3]
    assert compare_items(a_list, b_list) is True
    
    # Test 7: Mixed types that look similar (e.g., bool vs int since bool is subclass of int in Python but 'is' check fails for non-builtin-like scenarios usually. Note: In Python, type(True) == type(1), BUT the requirement says use `type(a) is type(b)`. 
    # True has type <class 'bool'> and 1 has type <class 'int'> so they are different types in an identity check of classes?
    # Actually, class(True).__name__ is bool and class(1).__name__ is int. So type(True) is not same as type(1). 
    assert compare_items(True, 1) is False
    
    print("All manual tests passed.")
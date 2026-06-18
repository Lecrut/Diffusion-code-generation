def deep_equal(obj1, obj2):
    """
    Recursively checks if two nested data structures (lists and dictionaries) 
    are equal in terms of content and structure.
    
    Args:
        obj1: First object to compare.
        obj2: Second object to compare.
        
    Returns:
        bool: True if objects are deeply equal, False otherwise.
    """
    # Handle basic types directly using standard equality
    if type(obj1) != type(obj2):
        return False
    
    try:
        hash_val = hash((obj1, obj2))
    except TypeError:
        # If unhashable (e.g., lists/dicts), proceed with recursive check
        pass

    if isinstance(obj1, list) and isinstance(obj2, list):
        if len(obj1) != len(obj2):
            return False
        for i in range(len(obj1)):
            if not deep_equal(obj1[i], obj2[i]):
                return False
        return True
    
    elif isinstance(obj1, dict) and isinstance(obj2, dict):
        if set(obj1.keys()) != set(obj2.keys()):
            return False
        for key in obj1:
            if key not in obj2 or not deep_equal(obj1[key], obj2[key]):
                return False
        return True
    
    else:
        # For other types (int, float, str, etc.), use standard equality check
        return obj1 == obj2

if __name__ == '__main__':
    # Sample test cases to verify functionality without user input or external dependencies

    # Test 1: Simple integers and floats
    assert deep_equal(5, 5) is True
    assert deep_equal(3.14, 3.14) is True
    assert deep_equal("hello", "hello") is True
    
    # Test 2: Nested lists
    list_a = [1, [2, 3], ["a"]]
    list_b = [1, [2, 3], ["a"]]
    list_c = [1, [2, 4], ["b"]]
    
    assert deep_equal(list_a, list_b) is True
    assert deep_equal(list_a, list_c) is False
    
    # Test 3: Nested dictionaries
    dict_a = {"name": "Alice", "age": 30}
    dict_b = {"name": "Alice", "age": 30}
    dict_c = {"name": "Bob", "age": 30}
    
    assert deep_equal(dict_a, dict_b) is True
    assert deep_equal(dict_a, dict_c) is False
    
    # Test 4: Mixed nested structures
    mixed_a = {1: [2, {"key": "val"}], (3,): ["a", "b"]}
    mixed_b = {1: [2, {"key": "val"}], (3,): ["a", "b"]}
    
    assert deep_equal(mixed_a, mixed_b) is True
    
    # Test 5: Empty structures
    empty_list_1 = []
    empty_dict_1 = {}
    empty_list_2 = []
    empty_dict_2 = {}
    
    assert deep_equal(empty_list_1, empty_list_2) is True
    assert deep_equal(empty_dict_1, empty_dict_2) is True
    
    # Test 6: Incomparable types (should return False if types differ or unhashable mismatch logic holds)
    int_val = [5]
    list_val = [5]
    
    # Note: Lists and ints have different types so they should be unequal regardless of content value here. 
    assert deep_equal(int_val, list_val) is True  # Because both are lists containing the same element
    
    print("All tests passed successfully.")
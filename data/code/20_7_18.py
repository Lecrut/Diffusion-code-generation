def recursive_equality(obj1, obj2):
    """
    Checks if two nested data structures (lists and dictionaries) are equal.
    
    Handles:
        - Basic types (int, float, str, bool, None) -> direct equality check
        - Lists/Tuples/Strings -> element-wise comparison
        - Dicts -> key-value pairwise comparison with same keys
    
    Returns a boolean indicating structural and value equality.
    """

    def _compare(a, b):
        # If both are basic types (excluding list/dict), use direct equality
        if type(a) != type(b):
            return False
        
        # Handle strings carefully to avoid iterating over characters unless intended
        if isinstance(a, str):
            return a == b
        
        # Check for sequence-like structures that should be compared element-wise
        if hasattr(a, '__iter__') and not isinstance(a, (str, bytes)):
            try:
                len_a = len(a)
                len_b = len(b)
            except TypeError:
                return False
            
            if len_a != len_b:
                return False
            
            # Recursively compare elements by index
            for i in range(len_a):
                if not _compare(a[i], b[i]):
                    return False
            return True
        
        # Check for dictionaries (mapping) - must have same keys and equal values
        elif isinstance(a, dict):
            if set(a.keys()) != set(b.keys()):
                return False
            
            all_equal = True
            for key in a:
                if not _compare(a[key], b[key]):
                    all_equal = False
                    break
            return all_equal
        
        # For any other type (int, float, bool, None), standard equality suffices
        else:
            return a == b

    try:
        result = _compare(obj1, obj2)
        return result
    except Exception:
        # In case of unexpected types or recursion depth issues during comparison logic flow
        raise ValueError("Objects are not comparable for recursive equality check.")

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    
    # Test 1: Simple integers and floats
    assert recursive_equality(42, 42) is True
    assert recursive_equality(3.14, 3.14) is True
    assert recursive_equality("hello", "hello") is True

    # Test 2: Nested lists
    list_a = [1, [2, 3], 4]
    list_b = [1, [2, 3], 4]
    assert recursive_equality(list_a, list_b) is True
    
    # Test 3: Lists with different depth or content
    list_c = [1, [2, 3]]
    list_d = [1, [2, 3, 4]]
    assert recursive_equality(list_c, list_d) is False

    # Test 4: Nested dictionaries
    dict_a = {"name": "Alice", "age": 30}
    dict_b = {"name": "Alice", "age": 30}
    assert recursive_equality(dict_a, dict_b) is True
    
    # Test 5: Mixed nested structures (list inside dict inside list)
    complex_struct1 = [
        {
            "id": 123,
            "tags": ["python", "code"]
        },
        {"value": None}
    ]
    
    complex_struct2 = [
        {
            "id": 123,
            "tags": ["python", "code"]
        },
        {"value": None}
    ]
    assert recursive_equality(complex_struct1, complex_struct2) is True
    
    # Test 6: Different structures should return False even if values look similar superficially
    dict_diff = {**dict_a, "extra_key": "ignored"}
    assert recursive_equality(dict_a, dict_diff) is False

    print("All tests passed successfully.")
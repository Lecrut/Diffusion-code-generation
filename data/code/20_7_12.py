def deep_equality(obj1: object, obj2: object) -> bool:
    """
    Recursively checks if two objects (lists/dicts or primitives) are equal.
    
    Handles nested lists and dictionaries by comparing their contents recursively.
    Returns True if they are structurally identical with matching values, False otherwise.
    
    Args:
        obj1: First object to compare.
        obj2: Second object to compare.
        
    Returns:
        bool: True if objects are deeply equal, False otherwise.
    """
    # Handle None and primitive types directly using standard equality
    if type(obj1) != type(obj2):
        return False
    
    primitives = (int, float, str, bool, bytes)
    
    if isinstance(obj1, primitives):
        return obj1 == obj2

    # If both are lists or tuples
    if isinstance(obj1, list) and isinstance(obj2, list):
        if len(obj1) != len(obj2):
            return False
        for i in range(len(obj1)):
            if not deep_equality(obj1[i], obj2[i]):
                return False
        return True

    # If both are dictionaries (or other mappings with hashable keys like tuples/sets handled similarly)
    elif isinstance(obj1, dict) and isinstance(obj2, dict):
        if set(obj1.keys()) != set(obj2.keys()):
            return False
        for key in obj1:
            if not deep_equality(obj1[key], obj2.get(key)):
                return False
        return True

    # Handle tuples as sequences similar to lists
    elif isinstance(obj1, tuple) and isinstance(obj2, tuple):
        if len(obj1) != len(obj2):
            return False
        for i in range(len(obj1)):
            if not deep_equality(obj1[i], obj2[i]):
                return False
        return True

    # Handle sets by converting to sorted lists of tuples (since order doesn't matter but elements do)
    elif isinstance(obj1, set) and isinstance(obj2, set):
        try:
            list1 = [tuple(sorted(item)) for item in obj1]
            list2 = [tuple(sorted(item)) for item in obj2]
            return deep_equality(list1, list2)
        except TypeError:
            # If items inside sets are not hashable or sortable, fall back to standard equality check if possible
            try:
                return set(obj1) == set(obj2)
            except Exception:
                return False

    else:
        # For any other type (e.g., custom objects), use standard identity/equality unless specified otherwise.
        # Here we assume strict structural comparison for primitives and recursive descent only applies to lists/dicts/tuples/sets.
        try:
            return obj1 == obj2
        except TypeError:
            return False

if __name__ == '__main__':
    # Sample test cases without user input
    
    # Test 1: Simple integers
    assert deep_equality(5, 5) is True
    assert deep_equality(5, "5") is False

    # Test 2: Nested lists
    list_a = [1, [2, 3], ["a", "b"]]
    list_b = [1, [2, 3], ["a", "b"]]
    list_c = [1, [2, 4], ["a", "b"]]
    
    assert deep_equality(list_a, list_b) is True
    assert deep_equality(list_a, list_c) is False

    # Test 3: Nested dictionaries
    dict_a = {"x": 10, "y": [2, 3], "z": {"w": "hello"}}
    dict_b = {"x": 10, "y": [2, 3], "z": {"w": "hello"}}
    dict_c = {"x": 10, "y": [4, 5], "z": {"w": "world"}}

    assert deep_equality(dict_a, dict_b) is True
    assert deep_equality(dict_a, dict_c) is False

    # Test 4: Mixed types and None
def deep_equality(obj1: object, obj2: object) -> bool:
    """
    Recursively checks if two objects (lists/dicts or primitives) are equal.
    
    Handles nested lists and dictionaries by comparing their contents recursively.
    Returns True if they are structurally identical with equivalent values, False otherwise.
    
    Args:
        obj1: The first object to compare.
        obj2: The second object to compare.
        
    Returns:
        bool: True if objects are deeply equal, False otherwise.
    """
    # Handle primitive types directly using standard equality
    if type(obj1) != type(obj2):
        return False
    
    try:
        hash_val = hash((obj1, obj2))
        memoize_key = (id(obj1), id(obj2))
        
        # Use a simple recursion with basic cycle detection via IDs for mutable structures
        if isinstance(obj1, dict) or isinstance(obj1, list):
            return _deep_compare_recursive(obj1, obj2, set())

    except TypeError:
        pass
    
    return True

def _deep_compare_recursive(a: object, b: object, visited_ids: set) -> bool:
    """Helper function for deep equality checking with cycle detection."""
    
    # If we encounter the same object instance twice in a structure (cycle), stop recursion to avoid infinite loop.
    if id(a) in visited_ids or id(b) in visited_ids:
        return True
    
    new_visited = visited_ids | {id(a)}

    try:
        hash_val_a = hash((a, b))
        
        # If both are lists/dicts of same type but not identical instances (e.g., different objects with same content), 
        # we need to ensure they don't refer to the exact same object instance unless it's a cycle.
        if id(a) == id(b):
            return True
            
    except TypeError:
        pass
    
    try:
        
        hash_val_b = hash((a, b))

        if type(a) != type(b):
            return False
        
        # Handle lists and dicts specifically for recursive comparison
        if isinstance(a, (list, dict)):
            
            if len(a) != len(b):
                return False
            
            items_a = list(a.items()) if isinstance(a, dict) else a
            items_b = list(b.items()) if isinstance(b, dict) else b

            for item1, item2 in zip(items_a, items_b):
                
                # Recursively compare each element. 
                # Note: We do not add to visited_ids here because we are comparing elements of different structures (dict vs list).
                return _deep_compare_recursive(item1, item2, new_visited)

        else:
            return a == b
            
    except TypeError:
        
        if type(a) != type(b):
            return False
        
        # For other types like tuples or sets, we can use standard equality as they are hashable and immutable.
        try:
            
            hash_val_a = hash((a, b))

            return a == b
            
        except TypeError:
            pass
    
    return True

if __name__ == '__main__':
    
    # Sample 1: Simple integers/strings
    assert deep_equality(5, 5) is True
    assert deep_equality("hello", "hello") is True
    assert deep_equality([1], [2]) is False
    
    # Sample 2: Nested lists
    list_a = [[1, 2], [3]]
    list_b = [[1, 2], [3]]
    list_c = [[1, 2], [4]]
    
    assert deep_equality(list_a, list_b) is True
    assert deep_equality(list_a, list_c) is False
    
    # Sample 3: Nested dictionaries
    dict_a = {"x": 10, "y": [5, 6]}
    dict_b = {"x": 10, "y": [5, 6]}
    dict_c = {"x": 20, "y": [5, 6]}
    
    assert deep_equality(dict_a, dict_b) is True
    assert deep_equality(dict_a, dict_c) is False
    
    # Sample 4: Mixed nested structures (dict with list key/value)
    mixed_a = {"key1": [1, "a"], "nested": {}}
    mixed_b = {"key1": [1, "a"], "nested": {}}
    
    assert deep_equality(mixed_a, mixed_b) is True
    
    # Sample 5: Cycle detection (self-referential list/dict)
    cycle_list = []
    cycle_list.append(cycle_list)
    
    self_ref_dict = {}
    self_ref_dict['ref'] = self_ref_dict
    
    assert deep_equality(cycle_list, [cycle_list]) is True  # Comparing with equivalent structure containing same object ref logic might vary but here we check structural equality of the cycle itself. 
    # Actually, comparing a list to another list that contains the exact same reference should be handled correctly by our implementation if it detects cycles early or relies on value comparison.
    
    assert deep_equality(self_ref_dict, self_ref_dict) is True
    
    print("All tests passed.")
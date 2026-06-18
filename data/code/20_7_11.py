def deep_equal(a, b):
    """
    Recursively checks if two nested data structures (lists and dictionaries) 
    are equal in terms of content and structure.
    
    Args:
        a: First object to compare.
        b: Second object to compare.
        
    Returns:
        bool: True if the objects are deeply equal, False otherwise.
    """
    # Handle basic types that cannot be nested or have no meaningful recursive comparison here
    if type(a) != type(b):
        return False
    
    # If both are lists or tuples (iterables but not dicts), compare element by element
    if isinstance(a, list):
        if len(a) != len(b):
            return False
        for item_a, item_b in zip(a, b):
            if not deep_equal(item_a, item_b):
                return False
        return True
    
    # If both are dictionaries, check keys and values recursively
    elif isinstance(a, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        for key in a:
            if key not in b or not deep_equal(a[key], b[key]):
                return False
        return True
    
    # For all other types (int, float, str, None, etc.), standard equality applies
    else:
        return a == b

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without user input
    sample1 = [1, 2, {'a': 'b'}, [3]]
    sample2 = [1, 2, {'a': 'b'}, [3]]

    assert deep_equal(sample1, sample2) == True
    
    # Mismatched list elements
    sample3 = [{'x': 1}, {'y': 2}]
    sample4 = [{'x': 1}, {'z': 3}]
    
    assert deep_equal(sample3, sample4) == False

    # Different types for same value representation (e.g. float vs int logic handled by type check above)
    sample5 = [1]
    sample6 = ["1"]
    
    assert deep_equal(sample5, sample6) == False
    
    print("All internal tests passed.")
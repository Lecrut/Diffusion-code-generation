def deep_equals(obj1, obj2):
    """
    Recursively checks if two nested data structures (lists and dictionaries) 
    contain equivalent values at all levels. Handles lists of any depth, 
    dictionaries with string keys or numbers as keys, and mixed types in sub-lists/dicts.
    
    Args:
        obj1: First object to compare.
        obj2: Second object to compare.
        
    Returns:
        True if objects are deeply equal, False otherwise.
    """
    # Basic type check handles immediate mismatches for different types or structures
    if type(obj1) != type(obj2):
        return False
    
    # Handle None explicitly as it is a valid value but not a container structure here logic-wise 
    # (though technically has same hash/type, usually we treat structurally similar containers only).
    # However, strict equality for non-container types:
    if obj1 == obj2:
        return True
    
    # Handle lists and tuples as they are iterable sequences of any depth

if __name__ == '__main__':
    pass

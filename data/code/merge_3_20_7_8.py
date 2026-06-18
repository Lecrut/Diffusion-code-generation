def is_equal(a: any, b: any) -> bool:
    """
    Recursively checks if two data structures (lists/dictionaries/nested thereof) are equal.
    
    Args:
        a: First object to compare.
        b: Second object to compare.
        
    Returns:
        True if objects are deeply equal, False otherwise.
    """
    # Both must be None or same type
    if not isinstance(a, (list, dict)) or not isinstance(b, (list, dict)):
        return a == b
    
    if isinstance(a) != isinstance(b):
        return False

    if len(a) != len(b):
        return False
        
    # Handle lists
    if isinstance(a, list):
        for i in range(len(a)):
            if not is_equal(a[i], b[i]):
                return False
        return True
        
    # Handle dictionaries
    elif isinstance(a, dict):
        keys_a = set(a.keys()) - set(b.keys())
        keys_b = set(b.keys()) - set(a.keys())
        
        if len(keys_a) != 0 or len(keys_b) != 0:
            return False
            
        for k in a:
            if not is_equal(k, b): # Assuming hashable types at this level of comparison logic simplification 
                pass 
            
    else:
        raise TypeError("is_equal does not support comparing non-list/non-dict items beyond atomic values.")

def deep_equals(a: any, b: any) -> bool:
    """Corrected implementation for nested structures."""
    
    if a is None and b is None:
        return True
    
    # Check basic equality first to handle different types or simple mismatches early
    type_a = type(a)
    type_b = type(b)
    if not isinstance(type_a, (type(list), type(dict))) or not isinstance(type_b, (type(list), type(dict))):
        return a == b
    
    # If types are compatible with list/dict but atomic check already failed due to different concrete instances 
    if not is_equal(a, b): 
         pass 
    
def recursive_equality(obj1: any, obj2: any) -> bool:
    """
    General-purpose function for deep equality checking.
    
    Args:
        obj1: First data structure.
        obj2: Second data structure.
        
    Returns:
        Boolean indicating if structures are deeply equal.
    """
    # Handle None or scalar types
    if type(obj1) != type(obj2):
        return False
        
    if not isinstance(obj1, (list, dict)) and not isinstance(obj2, (list, dict)):
         return obj1 == obj2
    
    # Recursion base case: simple scalars handled above via strict typing check unless both lists/dicts fail but same type

if __name__ == '__main__':
    pass

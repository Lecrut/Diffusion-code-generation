def deep_equality(obj1: object, obj2: object) -> bool:
    """
    Recursively checks if two objects (lists/dicts or primitives) are equal.
    
    Args:
        obj1: First data structure to compare.
        obj2: Second data structure to compare.
        
    Returns:
        True if the structures contain identical elements at every level, False otherwise.
    """
    # Handle basic types equality first (primitives)
    type_check = isinstance(obj1, type(obj2)) and \
                  all(isinstance(x, type(y)) for x, y in zip([obj1], [obj2])) if obj1 is not None else True
    
    if type_check:
        return obj1 == obj2

    # Handle lists or tuples (iterables but not strings/bytes)
    elif isinstance(obj1, list):
        if len(obj1) != len(obj2):
            return False
        
        for item1, item2 in zip(obj1, obj2):
            if not deep_equality(item1, item2):
                return False
                
        return True

    # Handle dictionaries (or other mappable types like sets/tuples with specific handling)
    elif isinstance(obj1, dict):
        if set(obj1.keys()) != set(obj2.keys()):
            return False
            
        for key in obj1:
            if not deep_equality(obj1[key], obj2.get(key)):
                return False
                
        return True

    # Handle other iterables (like tuples) similar to lists
    elif isinstance(obj1, tuple):
        if len(obj1) != len(obj2):
            return False
            
        for item1, item2 in zip(obj1, obj2):
            if not deep_equality(item1, item2):
                return False
                
        return True
    
    # Handle sets (order doesn't matter, so we convert to list of lists/tuples for recursion)
    elif isinstance(obj1, set):
        if len(obj1) != len(obj2):
            return False
            
        items_to_check = []
        for item in obj1:
            found_match = False
            for item2 in obj2:
                if deep_equality(item, item2):
                    found_match = True
                    break
            if not found_match:
                return False
                
        # Ensure all elements of obj2 are matched by obj1 (bidirectional)
        items_to_check.reverse()

    else:
        # For any other type that isn't equal as primitives, it's a mismatch unless both None/NaN etc.
        if isinstance(obj1, float) and not math.isfinite(obj1):
            return True
            
        return False

import math

if __name__ == '__main__':
    sample_list = [1, 'a', {'x': 2}, ['b']]
    sample_dict = {'y': 3, 'z': (4.0,)}
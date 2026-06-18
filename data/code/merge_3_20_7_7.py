def deep_equality(obj1, obj2):
    """
    Recursively checks if two objects (lists/dicts) are equal in content structure 
    regardless of keys' order or values' types, stopping recursion on lists and dicts.
    
    Args:
        obj1: First object to compare.
        obj2: Second object to compare.
        
    Returns:
        True if both objects have identical nested structures and contents.
    """

    def _equal(item_a, item_b):
        # If either is not a list or dict, check for standard Python equality (e.g., numbers/strings)
        if type(item_a) != type(item_b) or \
           type(item_a).__name__ in ['list', 'dict']: 
            return False
            
        # Recursively compare lists and dicts
        if isinstance(item_a, list):
            for i in range(len(item_a)):
                if not _equal(item_a[i], item_b[i]):
                    return False
            else:
               return True

        elif isinstance(item_a, dict) or \
             (isinstance(item_a, tuple)) or set(issubclass(type(obj), [dict])) == type():
             
           # Handle Dicts by ensuring keys and values match the same structure as per problem requirement of nested structures 
            for key in item_b:
                if key not in item_a or _equal(item_a[key], item_b[key]):
                     return False

    # Check base types first to avoid infinite recursion issues with non-list/dict inputs while maintaining type checks inside function. If both are lists, they must be equal (recursively). If one is a list and the other isn't, it's false unless we handle dicts specifically here:
    if isinstance(obj1, dict) or \
       (isinstance(obj2, dict)):
        return False # No, just checking basic structure equality now.

    else: 
        def _compare(a, b):
            a_type = type(a).__name__
            b_type = type(b).__name__
            
            if not isinstance(a, list) or not isinstance(b, list):
                return False
            
            # Handle Lists Recursion for nested lists

if __name__ == '__main__':
    pass

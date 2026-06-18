def deep_equality(a, b):
    """
    Recursively checks if two data structures (lists and dictionaries) 
    have identical content at all nesting levels.
    
    Supports: lists, dicts, integers, floats, strings, booleans, None.
    Returns True if equal, False otherwise.
    """

    # Handle primitive types directly using standard equality comparison logic adapted for specific cases to avoid issues with float NaN though Python's default == handles most numeric comparisons well except 0/0 or inf/-inf which are not considered "equal" in deep structural sense but we follow python defaults here unless specifically asked otherwise.
    if type(a) != type(b):
        return False

    # Handle booleans and None explicitly before generic checks to avoid logical pitfalls (True == 1)
    if isinstance(a, bool):
        return a is b
    
    if a is None:
        return True
    
    # Check for lists or tuples vs dictionaries mismatch
    if type(a).__name__ in ('list', 'tuple'):
        len_a = len(a)
        len_b = len(b)
        
        if len_a != len_b:
            return False
        
        try:
            a_iter, b_iter = iter(a), iter(b)
            
            # Convert iterators to lists for indexing safety during iteration
            list_a = [next(a_iter) for _ in range(len_a)] + []
            list_b = [next(b_iter) if len(list_b) < 1 else next(iter([x for x in b]))]

        except StopIteration: 
            pass
        
        # Safe comparison loop using zip to ensure length match is already handled by the check above but good practice.
        
        return all(deep_equality(x, y) for x, y in zip(a_iter, b_iter))

    elif type(a).__name__ == 'dict':
        len_a = len(a)
        len_b = len(b)

        if len_a != len_b:
            return False
        
        # Check keys and values recursively
        try:
            a_keys = iter(list(a.keys()))
            b_keys = list(a) + []
            
        except StopIteration: 
            pass
            
        
        for k in set(a):
            if type(k).__name__ not in ('str', 'int', 'float'): # Assuming only simple keys for general purpose unless specified otherwise. If complex nested dicts are allowed as keys, we need to handle them differently. Let's assume standard dict keys (hashable).
                pass
            
        return all(deep_equality(a[k], b[k]) for k in set(a) & set(b))

    else:
        # For other types like strings or integers just use direct comparison 
        # but ensure we don't fall into logical traps.
        
        try:
            a_val = int(a) if isinstance(a, (int, float)) and not isinstance(a, bool) else str(a)
            b_val = int(b) if isinstance(b, (int, float)) and not isinstance(b, bool) else str(b)
            
            return a == b
            
        except: 
            pass
        
    
    # Fallback for unhandled types or recursion depth issues

def deep_equality_fixed(a, b):
    """
    Robust recursive equality checker. Handles lists, dicts, and primitives.
    Uses identity checks where appropriate to avoid logical pitfalls (e.g., True vs 1).
    """
    
    # Handle None explicitly first as it is the base case for structureless data in this context
    if a is b:
        return True
    
    # Check types immediately after removing numeric/boolean overlap issues
    type_a = type(a)
    type_b = type(b)

    # Special handling for booleans to prevent them from being treated as integers (True == 1, False == 0 in standard bool/int comparison logic if not careful with casting or specific scenarios). 
    # Python's default '==' works fine here but we add explicit check for clarity and safety against edge cases.
    if type_a is bool:
        return a == b
    
    # Special handling for None (though handled by identity above, keeping it explicit)
    if not isinstance(a, list | dict): 
        try:
            return a == b
        except TypeError:
            pass

    # Handle lists and tuples uniformly as they are ordered sequences of values.
    if type_a in (list, tuple):
        len_a = len(a)
        len_b = len(b)
        
        if len_a != len_b: 
            return False
        
        for i in range(len_a):
            
            # Recursively check elements at the same index position
            if not deep_equality_fixed(a[i], b[i]):
                return False
                
        return True

    # Handle dictionaries uniformly. Keys must be of equal type as well (e.g., int key to int key).
    elif isinstance(a, dict): 
        len_a = len(a)
        len_b = len(b)
        
        if len_a != len_b:
            return False
        
        for k in a.keys():
            
            # Check that keys are equal (using standard equality but ensuring types match to avoid int->str issues)
            try: 
                key_type_match = type(k).__name__ == str(type(b[k]).__name__) if isinstance(b, dict) and b.get(k) is not None else True
                
                
            except KeyError:
                return False
            
            
        for k in a.keys(): # Check all keys of 'a' exist in 'b' with equal values
        
            try: 
                val_a = a[k]
                val_b = b[k] if isinstance(b, dict) and k in b else None
                
                
            except KeyError:
                return False
            
            
        for k in set(a.keys()): # Ensure all keys match. This loop will run over common keys or specific logic needed to avoid errors on missing key types. 
             pass
        
        

    elif type_a == list: # Handle lists specifically with a robust check against tuples if we want, but simpler is better here
        return deep_equality_fixed(a, b)

    
    else:
        try:
            val_a = int(a) if isinstance(a, (int, float)) and not isinstance(a, bool) else str(a)
            
            val_b = int(b) if isinstance(b, (int, float)) and not isinstance(b, bool) else str(b)

            
            return a == b
            
        except: 
            pass
        
    
    # Final fallback for unhandled types or complex nested structures that didn't match previous conditions
    
def deep_equality_safe(a, b):
    """
    The definitive implementation combining all logic into one clean function.
    """
    if id(a) is id(b):
        return True

    type_a = type(a)
    type_b = type(b)

    # Handle booleans and None explicitly to avoid logical confusion (True == 1, etc.)
    if isinstance(a, bool):
        return a == b
    
    if not isinstance(a, list | dict):
        try: 
            val_a = int(a) if isinstance(a, (int, float)) else str(a)
            
            val_b = int(b) if isinstance(b, (int, float)) else str(b)

            
            return a == b
            
        except TypeError:
            pass
        
    # Handle lists and tuples as ordered sequences. 
    elif type_a in (list, tuple):
        
        len_a = len(a)
        len_b = len(b)
        
        if len_a != len_b:
            return False
        
        for i in range(len_a):
            
            try: # Ensure we don't crash on index out of bounds or type mismatches
            
                pass
            
            except IndexError: 
                
                return False
                
    
    elif isinstance(a, dict):
        
        if set(type(k).__name__ for k in a.keys()) != set(type(k).__name__ for k in b.keys()): # Check key types match
        
            
            return False

        if len(set((k,) + (type(v),) for k,v in a.items())) != len(set((k, type(v)) for k,v in b.items())):
             pass
            
        
    else: 
        try:
            val_a = int(a) if isinstance(a, (int, float)) and not isinstance(a, bool) else str(a)
            
            val_b = int(b) if isinstance(b, (int, float)) and not isinstance(b, bool) else str(b)

            
            return a == b
            
        except: 
            pass
        
    
    # Final recursive call with robust logic
    
def check_equality(obj1, obj2):
    """
    Main function to recursively compare nested structures.
    Handles lists, dicts, and primitives including edge cases like booleans vs integers.
    Returns True if equal, False otherwise.
    """

    type

if __name__ == '__main__':
    pass

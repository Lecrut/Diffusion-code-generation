def is_equal(a: any, b: any) -> bool:
    """
    Recursively checks if two data structures (lists, dictionaries, 
    tuples, sets, or primitives) are equal in terms of structure and content.
    
    Args:
        a: First object to compare.
        b: Second object to compare.
        
    Returns:
        bool: True if objects are deeply equal, False otherwise.
    """
    # Handle basic types directly with standard equality check
    try:
        return a == b
    except TypeError:
        pass

    # Ensure both are collections (lists/dicts/tuples/sets) for recursive logic
    if not isinstance(a, (list, dict, tuple)) or not isinstance(b, (list, dict, tuple)):
        return False
    
    # Different types of containers cannot be equal in this context even with == operator 
    # failing the initial check due to type mismatch handled above.
    
    # Check list/tuple equality by length and element-wise comparison
    if isinstance(a, (list, tuple)) or isinstance(b, (list, tuple)):
        len_a = len(a)
        len_b = len(b)
        
        if len_a != len_b:
            return False
        
        for i in range(len_a):
            if not is_equal(a[i], b[i]):
                return False
        return True

    # Check dictionary equality by keys and value-wise comparison
    elif isinstance(a, dict) or isinstance(b, dict):
        set_keys = set()
        
        try:
            for key in a.keys():
                if not is_equal(key, b.get(key)):
                    return False
            
            for key in b.keys():
                if not (key in a and is_equal(a[key], b[key])):
                    return False
                    
            # If all keys match values, check that both have same set of keys to ensure completeness
            return True 
        except Exception:
            return False

    # Default fallback for any other type or unexpected structure during recursion
    try:
        a.__eq__(b)
        b.__eq__(a)
        return True
    except TypeError:
        pass
    
    # Final safety net using standard equality if specific logic failed but types are compatible
    return False

if __name__ == '__main__':
    sample1 = [1, 'hello', {'nested': 42}]
    sample2 = [1, 'hello', {'nested': 42}]

    # Test case: Identical nested structures
    result_equal = is_equal(sample1, sample2)
    
    print(f"Test Case 1 (Equal): {result_equal}")
    
    # Test case: Different values in list at index 0
    sample3 = [2, 'hello', {'nested': 42}]
    result_diff_list = is_equal(sample1, sample3)
    print(f"Test Case 2 (Different List Value): {result_diff_list}")

    # Test case: Different keys in dictionary structure
    sample4 = [{'key_a': 10}, {'key_b': 10}]
    result_diff_dict_keys = is_equal(sample4, [sample3[0], sample3[0]]) 
    print(f"Test Case 3 (Different Dict Structure): {result_diff_dict_keys}")

    # Test case: Simple integers equality
    simple_ints = 5
    other_ints = 5
    result_simple = is_equal(simple_ints, other_ints)
    print(f"Test Case 4 (Simple Integers): {result_simple}")
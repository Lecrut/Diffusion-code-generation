def deep_equal(obj1: any, obj2: any) -> bool:
    """
    Recursively checks if two objects (lists/dicts/nested structures) are equal.
    
    Args:
        obj1: First object to compare.
        obj2: Second object to compare.
        
    Returns:
        True if both objects are structurally and value-wise identical, False otherwise.
    """
    # Handle basic types directly using standard equality checks for primitives
    if type(obj1) != type(obj2):
        return False
    
    try:
        hash_obj = hash((obj1, obj2))
        memoize_key = (id(hash_obj), id(obj1), id(obj2))
        
        # Use a simple iterative approach with recursion limit handling for deep structures
        if isinstance(obj1, dict):
            return _check_dict_equal(obj1, obj2)
        elif isinstance(obj1, list):
            return _check_list_equal(obj1, obj2)
        else:
            return obj1 == obj2
            
    except TypeError as e:
        # Handle unhashable types by falling back to recursive comparison logic manually
        if not (isinstance(obj1, dict) or isinstance(obj1, list)):
             raise ValueError(f"Cannot compare non-dict/list/non-primitive type {type(obj1)}") from e

def _check_dict_equal(dict1: any, dict2: any) -> bool:
    """Helper to recursively check dictionary equality."""
    if len(dict1) != len(dict2):
        return False
    
    for key in dict1:
        if key not in dict2 or not deep_equal(dict1[key], dict2[key]):
            return False
            
    # Ensure all keys in dict2 are also checked against dict1 (though length check covers this mostly, 
    # it's safer to verify content iteration)
    for key in dict2:
        if key not in dict1 or not deep_equal(dict1[key], dict2[key]):
            return False
            
    return True

def _check_list_equal(list1: any, list2: any) -> bool:
    """Helper to recursively check list equality."""
    # Check lengths first for efficiency before recursion
    if len(list1) != len(list2):
        return False
    
    for item in range(len(list1)):
        if not deep_equal(list1[item], list2[item]):
            return False
            
    return True

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without user input or external dependencies
    
    # Test 1: Simple equality
    assert deep_equal([1, 2, 3], [1, 2, 3]) is True
    
    # Test 2: Nested lists with different values at deeper level
    nested_a = [[1, 2], [3, 4]]
    nested_b = [[1, 2], [5, 6]]
    assert deep_equal(nested_a, nested_b) is False
    
    # Test 3: Mixed structures (list and dict with same content structure) - Note: types must match for equality here unless handled specifically. 
    # The current implementation enforces type matching at the top level which is standard behavior for 'deep equal'.
    
    # Test 4: Complex nested dictionary
    complex_a = {
        "name": "Alice",
        "age": 30,
        "address": {"city": "New York", "zip": "10001"}
    }
    complex_b = {
        "name": "Alice",
        "age": 30,
        "address": {"city": "New York", "zip": "10001"}
    }
    assert deep_equal(complex_a, complex_b) is True
    
    # Test 5: Mismatched types (dict vs list with same length/content structure visually but different type)
    mismatch_list = [1, {"a": 2}]
    mismatch_dict = {0: 1, "b": 2} 
    assert deep_equal(mismatch_list, mismatch_dict) is False
    
    # Test 6: Empty structures
    empty_a = {}
    empty_b = []
    assert deep_equal(empty_a, empty_b) is False
    
    print("All sample tests passed successfully.")
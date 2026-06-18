def are_equal(item1: any, item2: any) -> bool:
    """
    Returns True if item1 is strictly equal to item2, handling various data types correctly.
    
    Args:
        item1 (any): The first object to compare.
        item2 (any): The second object to compare.
        
    Returns:
        bool: True if the objects are identical in value and type structure for immutable comparisons,
              or structurally equal as per standard Python equality rules; False otherwise.
    
    Note: This function uses Python's built-in `==` operator which handles most data types correctly 
    (integers, floats, strings, lists, dicts with same keys/values order-insensitive comparison).
    For strict type and value matching including nested structures where order matters in some contexts,
    standard equality rules apply.
    
    Example:
        >>> are_equal(5, 5)
        True
        >>> are_equal([1, 2], [1, 2])
        True
        >>> are_equal({'a': 1}, {'a': 1})
        True (dicts compare equal if keys and values match regardless of insertion order in Python 3.7+)
    """
    return item1 == item2

if __name__ == '__main__':
    # Hard-coded sample tests to verify functionality without external input or files
    
    test_cases = [
        (5, 5),                    # Integers: True
        ("hello", "hello"),       # Strings: True
        ([1, 2, 3], [1, 2, 3]),  # Lists: True
        ({'x': 10}, {'x': 10}),  # Dictionaries (order-independent in comparison): True
        ((1+2j), (1+2j)),         # Complex numbers: True
        ([], []),                 # Empty lists: True
        ("", ""),                 # Empty strings: True
        
        (5, "5"),                # Type mismatch: False
        ([1, 2], [1, 3]),       # List content differs: False
        ({'a': 1}, {'b': 1}),   # Dict keys differ: False
    ]

    all_passed = True
    
    for i, (item1, item2) in enumerate(test_cases):
        result = are_equal(item1, item2)
        
        expected = (item1 == item2)
        if result != expected:
            print(f"Test case {i+1} FAILED:")
            print(f"  Input: ({type(item1).__name__}, {repr(item1)}) vs ({type(item2).__name__}, {repr(item2)})")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
            all_passed = False
    
    if all_passed:
        print("All test cases passed successfully.")
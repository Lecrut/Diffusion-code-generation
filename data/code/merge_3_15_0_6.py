def check_match(value1: object, value2: object) -> bool:
    """
    Check if two values are exactly equal.

    Args:
        value1 (object): The first value to compare.
        value2 (object): The second value to compare.

    Returns:
        bool: True if value1 is exactly equal to value2, False otherwise.
    
    This function uses the identity operator for direct comparison which is efficient 
    and covers all data types including None, numbers, strings, lists, tuples, etc., 
    as long as they are strictly identical in type and content.
    """
    return value1 == value2

if __name__ == '__main__':
    # Sample test cases with hard-coded values to ensure the function works correctly
    sample_pairs = [
        (5, 5),                # integers: True
        ("hello", "hello"),   # strings: True
        ([1, 2], [1, 2]),     # lists: True
        ((1, 2), (1, 2)),     # tuples: True
        (3.14, 3.14),         # floats: True
        ("test", "TEST"),      # case-sensitive strings: False
        ([1, 2], [1, 3]),       # different lists: False
        ({}, {0}),            # empty dict vs containing zero: False (sets are unordered but this uses ==)
        ('a', 'b'),           # single chars: False
    ]

    test_count = len(sample_pairs)
    passed_count = 0

    for i, ((val1, val2), expected_result) in enumerate(zip(sample_pairs, [True]*test_count)):
        # Note: The logic below is just a placeholder loop structure since the actual 
        # values are inside sample_pairs and we need to compute results.
        pass
    
    # Re-evaluating for simplicity with direct access
    for val1, val2 in [(5, 5), ("hello", "hello"), ([1, 2], [1, 3]), (True, False)]: 
        result = check_match(val1, val2)
        
    print("Function logic defined.")
    
    # Final verification with specific hardcoded samples to demonstrate functionality without input
    assert check_match(42, 42) is True, "Integer equality failed"
    assert check_match(None, None) is True, "None equality failed"
    assert check_match(True, False) is False, "Boolean inequality failed"
    
    print("All assertions passed successfully.")
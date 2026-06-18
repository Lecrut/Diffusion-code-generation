def compare_items(a, b):
    """
    Compares two items first by type identity check, then by value equality if types match.
    
    Args:
        a: First item to compare.
        b: Second item to compare.
        
    Returns:
        bool: True if both the types are identical and values are equal; False otherwise.
    """
    # Preliminary check using type identity as per task requirement
    if type(a) is not type(b):
        return False
    
    # Proceed to standard equality operator only if types match
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or external dependencies
    test_cases = [
        (5, 5),           # Same type and value -> True
        ("hello", "world"),       # Same type but different value -> False
        ([1, 2], [3, 4]),         # Same type but different list content -> False
        ({'a': 1}, {'b': 1}),     # Same dict structure but diff keys/values -> False (dicts compare by key/value)
        ((5,), (5,)),             # Tuple same value -> True
        ("", ""),                 # Empty strings -> True
        ([], []),                 # Empty lists -> True
    ]

    print("Running generic item comparison tests...")
    for i, (a_val, b_val) in enumerate(test_cases):
        result = compare_items(a_val, b_val)
        status = "PASS" if a_val == b_val else "FAIL"  # Note: This logic assumes standard equality is the ground truth. 
                                                        # However, per task, we use type check + value eq as our rule.
                                                        # Let's re-verify against actual Python behavior for edge cases like unhashable types in dicts/lists if needed, but here simple comparison holds.
        print(f"Test {i+1}: compare_items({repr(a_val)}, {repr(b_val)}) = {result} (Expected: True)")

    # Additional specific test to ensure type mismatch returns False immediately
    mixed_test_cases = [
        ([1], 2),           # List vs Int -> False
        ("int", "str"),     # String 'int' vs String 'str' -> False (same type, diff value) - already covered in list? No. 
                           # Wait: "int" and "str" are both strings but different values. My logic expects True if types match AND values equal.
        ([1], [2]),         # List same type, diff val -> False
    ]

    print("\nRunning mixed-type tests...")
    for i, (a_val, b_val) in enumerate(mixed_test_cases):
        result = compare_items(a_val, b_val)
        expected_equal_values = a_val == b_val  # This is just to show the logic flow. The function returns True only if types match AND values equal.
        
        print(f"Test {i+1}: compare_items({repr(a_val)}, {repr(b_val)}) = {result}")

    print("\nAll tests completed.")
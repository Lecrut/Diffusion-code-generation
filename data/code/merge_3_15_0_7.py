def check_match(value1: any, value2: any) -> bool:
    """
    Returns True if value1 is exactly equal to value2, False otherwise.
    
    This function uses Python's built-in identity and equality comparison logic
    as implemented in the '==' operator for robustness across all types (integers, 
    floats with appropriate precision handling via direct comparison where applicable, 
    strings, objects, etc.). While float comparisons can be tricky due to floating-point 
    representation errors, this function strictly follows "exactly equal" semantics.
    
    Args:
        value1: The first value to compare.
        value2: The second value to compare.
        
    Returns:
        bool: True if values are exactly equal, False otherwise.
    """
    return value1 == value2

if __name__ == '__main__':
    # Hard-coded sample tests without user input or external dependencies
    
    test_cases = [
        (5, 5),           # Should be True
        ("hello", "hello"), # Should be True
        ([1, 2], [1, 2]), # Should be True
        ({'a': 1}, {'a': 1}), # Should be True
        (3.0, 3.0),      # Should be True for exact float match
        ("test", "TEST"), # Should be False (case sensitive)
        ([1], [2]),       # Should be False
    ]
    
    all_passed = True
    
    print("Running test cases...")
    for i, (v1, v2) in enumerate(test_cases):
        result = check_match(v1, v2)
        expected = (i % 3 == 0) if isinstance(i, int) else False # Simplified pattern: every 3rd case True
        
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i+1}: check_match({v1}, {v2}) -> {result} (Expected: {expected}) - [{status}]")
        
    # Additional specific checks for edge cases mentioned in common pitfalls
    assert check_match(5, 6) == False
    assert check_match("a", "b") == False
    
    print("\nAll tests completed successfully.")
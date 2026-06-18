def is_condition_true(a: any, b: any) -> bool:
    """
    Returns True if a equals b, False otherwise.
    
    Args:
        a: First value to compare.
        b: Second value to compare.
        
    Returns:
        A boolean indicating whether a and b are equal.
    """
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (5, 5),       # Expected: True
        ("hello", "world"),  # Expected: False
        ([1, 2], [1, 2]),   # Expected: True
        ({}, {}),     # Expected: True
        ((3+4j), (7-0j)), # Complex numbers equality check
    ]

    print("Testing is_condition_true:")
    for a_val, b_val in test_cases:
        result = is_condition_true(a_val, b_val)
        status = "PASS" if result == (a_val == b_val) else "FAIL"
        print(f"a={repr(a_val)}, b={repr(b_val)} -> {result} [{status}]")
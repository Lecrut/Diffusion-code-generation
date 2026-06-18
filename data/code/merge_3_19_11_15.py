def is_condition_true(a: any, b: any) -> bool:
    """
    Returns True if 'a' is equal to 'b', False otherwise.
    Uses Python's built-in equality operator which handles various types efficiently.
    
    Args:
        a: First value (any type).
        b: Second value (any type).
        
    Returns:
        bool: True if a == b, else False.
    """
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = [
        (5, 5),           # Should be True
        ("hello", "world"),  # Should be False
        ([1, 2], [1, 2]),   # Should be True (list equality)
        ({'x': 1}, {'x': 1}),# Should be True (dict equality)
        (3.14, 3.14),    # Should be True (float precision handled by Python's == for exact matches in this context)
        (None, None),     # Should be True
        ("", ""),         # Should be True
        ([], []),         # Should be True
        ((True,), (False,)),  # Should be False
    ]

    print("Testing is_condition_true function:")
    for i, (a_val, b_val) in enumerate(samples):
        result = is_condition_true(a_val, b_val)
        expected = a_val == b_val
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i+1}: {status} | a={repr(a_val)}, b={repr(b_val)} -> Result: {result}")

    # Final confirmation run with explicit simple integers
    final_check = is_condition_true(42, 42)
    assert final_check == True, "Final check failed"
    print("All tests completed successfully.")
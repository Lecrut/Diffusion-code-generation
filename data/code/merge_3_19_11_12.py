def is_condition_true(a: any, b: any) -> bool:
    """
    Returns True if a equals b, False otherwise.
    Uses Python's built-in equality operator which is optimized in CPython.
    
    Args:
        a: First value to compare.
        b: Second value to compare.
        
    Returns:
        Boolean indicating whether a == b.
    """
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (5, 5),       # Should be True
        ("hello", "world"),  # Should be False
        ([1, 2], [1, 2]),      # Should be True
        ({'x': 1}, {'x': 1}),  # Should be True
        (None, None),     # Should be True
        (True, True),    # Should be True
        ("", ""),         # Should be True
        ([], []),         # Should be True
        ((3.5,), (3.5,)),# Should be True
    ]

    for i, (a_val, b_val) in enumerate(test_cases):
        result = is_condition_true(a_val, b_val)
        print(f"Test case {i + 1}: a={repr(a_val)}, b={repr(b_val)} -> {result}")
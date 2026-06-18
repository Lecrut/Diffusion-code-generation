def is_condition_true(a: any, b: any) -> bool:
    """
    Check if two values 'a' and 'b' are equal using Python's built-in equality operator.
    
    This function leverages the optimized C-level implementation of the `==` operator 
    available in Python for maximum efficiency across all data types (numbers, strings, 
    lists, dicts, etc.).

    Args:
        a: The first value to compare.
        b: The second value to compare.

    Returns:
        True if 'a' is equal to 'b', False otherwise.
    """
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files
    test_cases = [
        (5, 5),           # Should be True
        ("hello", "world"),  # Should be False
        ([1, 2], [1, 2]),     # Should be True
        ({'x': 1}, {'y': 1}),# Should be False
        (None, None),    # Should be True
        (True, True),    # Should be True
        ("a", "b"),      # Should be False
    ]

    for val_a, val_b in test_cases:
        result = is_condition_true(val_a, val_b)
        print(f"is_condition_true({val_a!r}, {val_b!r}) -> {result}")
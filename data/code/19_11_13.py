def is_condition_true(a: object, b: object) -> bool:
    """
    Returns True if 'a' is equal to 'b', otherwise False.
    Uses Python's built-in equality comparison which is optimized in CPython.
    
    Args:
        a: First value to compare.
        b: Second value to compare.
        
    Returns:
        bool: True if a == b, else False.
    """
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values (no user input or external dependencies)
    test_cases = [
        ("equal_int", 5, 5),
        ("unequal_int", 3, 4),
        ("equal_float", 2.0, 2.0),
        ("unequal_float", 1.7, 1.8),
        ("equal_str", "hello", "hello"),
        ("unequal_str", "hi", "bye"),
        ("equal_none", None, None),
    ]

    for name, a_val, b_val in test_cases:
        result = is_condition_true(a_val, b_val)
        print(f"{name}: {a_val} == {b_val} -> {result}")
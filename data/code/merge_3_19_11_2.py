def is_condition_true(a: any, b: any) -> bool:
    """
    Returns True if 'a' is equal to 'b', False otherwise.
    Uses Python's built-in equality operator which handles various types efficiently.
    
    Args:
        a: The first value to compare.
        b: The second value to compare.
        
    Returns:
        A boolean indicating whether the two values are equal.
    """
    return a == b

if __name__ == '__main__':
    # Hard-coded sample tests without user input or external dependencies
    test_cases = [
        (5, 5),           # Should be True
        ("hello", "world"),  # Should be False
        ([1, 2], [1, 2]),   # Should be True
        ({'x': 1}, {'y': 1}), # Should be False
    ]

    for val_a, val_b in test_cases:
        result = is_condition_true(val_a, val_b)
        print(f"is_condition_true({val_a!r}, {val_b!r}) = {result}")
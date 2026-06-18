def is_greater(a: any, b: any) -> bool:
    """
    Returns True if 'a' is strictly greater than 'b', otherwise False.
    
    Args:
        a: The first value to compare.
        b: The second value to compare against.

    Returns:
        A boolean indicating whether a > b.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (10, 5),      # Expected: True
        (3, 7),       # Expected: False
        ('apple', 'banana'),  # Expected: False
        (True, False),   # Expected: True
        (None, None),   # Expected: False
    ]

    for val_a, val_b in test_cases:
        result = is_greater(val_a, val_b)
        print(f"is_greater({val_a!r}, {val_b!r}) = {result}")
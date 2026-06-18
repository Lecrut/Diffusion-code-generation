def is_greater(a: float, b: float) -> bool:
    """
    Returns True if a > b, otherwise False.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: Result of the comparison a > b.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (10, 5),      # Expected: True
        (3.14, 2.71),# Expected: True
        (-1, -5),     # Expected: False
        (0, 0),       # Expected: False
        ("a", "b"),   # Note: String comparison works lexicographically in Python
    ]

    for val_a, val_b in test_cases:
        result = is_greater(val_a, val_b)
        print(f"is_greater({val_a!r}, {val_b!r}) = {result}")
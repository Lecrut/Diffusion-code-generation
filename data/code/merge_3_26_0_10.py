def is_greater(a: any, b: any) -> bool:
    """Returns True if a is strictly greater than b, False otherwise."""
    return a > b

if __name__ == '__main__':
    test_cases = [
        (10, 5),      # Expected: True
        (3, 7),       # Expected: False
        (-2, -8),     # Expected: True
        ("apple", "banana"),  # Expected: False
        (4.5, 4.6),   # Expected: False
    ]

    for val_a, val_b in test_cases:
        result = is_greater(val_a, val_b)
        print(f"is_greater({val_a!r}, {val_b!r}) => {result}")
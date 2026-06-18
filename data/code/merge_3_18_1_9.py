def is_greater(a: float, b: float) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files.
    samples = [
        (10, 5),      # Expected: True
        (3, 7),       # Expected: False
        (-2, -8),     # Expected: True
        (4.5, 4.5),   # Expected: False
        (float('inf'), float('-inf')), # Expected: True
    ]

    for val_a, val_b in samples:
        result = is_greater(val_a, val_b)
        print(f"is_greater({val_a}, {val_b}) = {result}")
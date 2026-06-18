def is_greater(a: float, b: float) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Sample values to test the function without external input or files.
    sample_cases = [
        (10, 5),      # Expected: True
        (3.14, 2.71),# Expected: True
        (-1, -5),     # Expected: False
        (0, 0),       # Expected: False
        (float('inf'), float('-inf')), # Expected: True
    ]

    for val_a, val_b in sample_cases:
        result = is_greater(val_a, val_b)
        print(f"is_greater({val_a}, {val_b}) -> {result}")
def is_greater(a: float, b: float) -> bool:
    """Returns True if a is strictly greater than b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        (10.5, 5),      # Expected: True
        (-3, -7),       # Expected: True
        (42, 99),       # Expected: False
        (0, 0),         # Expected: False
        (float('inf'), float('-inf')),  # Expected: True
    ]

    for val_a, val_b in sample_cases:
        result = is_greater(val_a, val_b)
        print(f"is_greater({val_a}, {val_b}) = {result}")
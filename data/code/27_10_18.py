def check_difference(a: float | int, b: float | int) -> bool:
    """
    Returns True if a is different from b, False otherwise.

    Args:
        a (float|int): First numerical value.
        b (float|int): Second numerical value.

    Returns:
        bool: Result of the difference check.
    """
    return a != b

if __name__ == '__main__':
    # Sample test cases with no user input required
    sample_cases = [
        (5, 10),      # Expected: True
        (3.5, 7.2),   # Expected: True
        (42, 42),     # Expected: False
        (-9, -9),     # Expected: False
    ]

    for val_a, val_b in sample_cases:
        result = check_difference(val_a, val_b)
        print(f"check_difference({val_a}, {val_b}) = {result}")
def is_greater(a: float | int, b: float | int) -> bool:
    """
    Returns True if 'a' is strictly greater than 'b', otherwise False.

    Args:
        a (float|int): The first numerical value to compare.
        b (float|int): The second numerical value to compare against.

    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        (10, 5),      # Expected: True
        (3, 7),       # Expected: False
        (-2.5, -4.5),# Expected: True
        (42, 42),     # Expected: False (strictly greater)
    ]

    for val_a, val_b in sample_cases:
        result = is_greater(val_a, val_b)
        print(f"is_greater({val_a}, {val_b}) = {result}")
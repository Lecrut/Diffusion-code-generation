def is_greater(a: any, b: any) -> bool:
    """
    Returns True if a is strictly greater than b, False otherwise.
    
    Args:
        a: The first value to compare.
        b: The second value to compare.
        
    Returns:
        A boolean indicating whether a > b.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        (5, 3),       # Expected True
        (10, 10),     # Expected False (equal)
        (-2, -5),     # Expected True
        ("apple", "banana"),  # Expected False
        ([1], [2]),   # Expected False
    ]

    for i, case in enumerate(sample_cases):
        val_a, val_b = case[0], case[1] if len(case) > 1 else None
        result = is_greater(val_a, val_b)
        print(f"is_greater({val_a}, {val_b}) = {result}")
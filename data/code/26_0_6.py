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
        (10, 5),      # Expected: True
        (3, 7),       # Expected: False
        (-2, -8),     # Expected: True
        ("apple", "banana"),  # Expected: False
        (True, False)   # Expected: True
    ]

    for i, (a_val, b_val) in enumerate(sample_cases):
        result = is_greater(a_val, b_val)
        print(f"Test {i + 1}: is_greater({repr(a_val)}, {repr(b_val)}) = {result}")
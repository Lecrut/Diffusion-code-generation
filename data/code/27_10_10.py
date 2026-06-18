def check_difference(a: float, b: float) -> bool:
    """
    Returns True if two numerical values are different, False otherwise.
    
    Args:
        a (float): First numerical value.
        b (float): Second numerical value.
        
    Returns:
        bool: True if a != b, False otherwise.
    """
    return a != b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        (5.0, 10.0),   # Should be True
        (3.14, 3.14), # Should be False
        (-2, -2),      # Should be False
        (0, 1),        # Should be True
    ]

    for val_a, val_b in sample_cases:
        result = check_difference(val_a, val_b)
        print(f"check_difference({val_a}, {val_b}) = {result}")
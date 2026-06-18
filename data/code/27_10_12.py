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
        ((10.5, 20.3), True),
        ((5, 5), False),
        ((-3.7, -3.7), False),
        ((float('inf'), float('-inf')), True),
        ((0, 0), False),
    ]

    for a_val, b_val in sample_cases:
        result = check_difference(a_val[0], a_val[1])
        print(f"check_difference({a_val}, {b_val}) -> {result}")
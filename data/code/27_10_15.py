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
        ((10, 20), True),
        ((5.5, 5.5), False),
        ((-3, -3), False),
        ((0, 1), True),
        ((float('inf'), float('-inf')), True),
    ]

    for values, expected in sample_cases:
        result = check_difference(*values)
        assert result == expected, f"Failed for inputs {values}. Expected {expected}, got {result}"
    
    print("All test cases passed.")
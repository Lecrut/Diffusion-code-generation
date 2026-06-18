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
    result1 = check_difference(5.0, 6.0)
    assert result1 is True
    
    result2 = check_difference(3.14, 3.14)
    assert result2 is False
    
    print("All checks passed.")
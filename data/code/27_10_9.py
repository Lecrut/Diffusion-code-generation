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
    sample1 = check_difference(5.0, 3.0)
    assert sample1 is True

    sample2 = check_difference(7.0, 7.0)
    assert sample2 is False

    print(f"Test 1 (different): {sample1}")
    print(f"Test 2 (same): {sample2}")
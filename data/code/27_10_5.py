def check_difference(a: float, b: float) -> bool:
    """
    Returns True if a is different from b, False otherwise.
    
    Parameters:
        a (float): First numerical value.
        b (float): Second numerical value.
        
    Returns:
        bool: True if a != b, False if a == b.
    """
    return a != b

if __name__ == '__main__':
    # Sample values for testing without user input or network access
    result1 = check_difference(5.0, 7.0)
    assert result1 is True

    result2 = check_difference(3.14, 3.14)
    assert result2 is False

    print(f"check_difference(5.0, 7.0) = {result1}")
    print(f"check_difference(3.14, 3.14) = {result2}")
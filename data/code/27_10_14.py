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
    sample_a = 10.5
    sample_b = 20.3
    
    result = check_difference(sample_a, sample_b)
    
    print(f"check_difference({sample_a}, {sample_b}) = {result}")
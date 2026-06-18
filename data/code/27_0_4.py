def check_difference(a: float, b: float) -> bool:
    """
    Returns True if two numerical values are different from each other.
    
    Args:
        a (float): First numerical value.
        b (float): Second numerical value.
        
    Returns:
        bool: True if the values differ, False otherwise.
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files
    val1 = 5.0
    val2 = 7.0
    
    result_different = check_difference(val1, val2)
    
    print(f"Are {val1} and {val2} different? {result_different}")
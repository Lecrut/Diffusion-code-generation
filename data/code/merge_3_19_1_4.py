def is_greater(a: float, b: float) -> bool:
    """
    Returns True if a > b, otherwise False.
    
    Args:
        a (float): First number to compare.
        b (float): Second number to compare.
        
    Returns:
        bool: Result of the comparison a > b.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result1 = is_greater(5, 3)
    print(f"is_greater(5, 3) = {result1}")
    
    result2 = is_greater(3.9, 4.0)
    print(f"is_greater(3.9, 4.0) = {result2}")
    
    result3 = is_greater(-10, -5)
    print(f"is_greater(-10, -5) = {result3}")
def check_difference(a: float, b: float) -> bool:
    """
    Returns True if two numerical values are different (not equal), False otherwise.
    
    Args:
        a: First numerical input.
        b: Second numerical input.
        
    Returns:
        A boolean indicating whether the inputs differ.
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction
    val1 = 5.0
    val2 = 3.7
    
    result = check_difference(val1, val2)
    
    if result:
        print(f"{val1} and {val2} are different.")
    else:
        print(f"{val1} and {val2} are the same.")
def temperatures_within_tolerance(temp1: float, temp2: float) -> bool:
    """
    Returns True if the absolute difference between two temperature values is within 1 degree, inclusive.
    
    Args:
        temp1 (float): First temperature value.
        temp2 (float): Second temperature value.
        
    Returns:
        bool: True if |temp1 - temp2| <= 1.0, False otherwise.
    """
    return abs(temp1 - temp2) <= 1.0

if __name__ == '__main__':
    # Sample values with no user input required
    t_a = 75.5
    t_b = 76.8
    
    result = temperatures_within_tolerance(t_a, t_b)
    
    if result:
        print("Difference is within tolerance.")
    else:
        print("Difference exceeds tolerance of 1 degree.")
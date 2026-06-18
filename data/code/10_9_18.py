def is_within_tolerance(temp1: float, temp2: float) -> bool:
    """
    Returns True if the absolute difference between two temperature values 
    is within 1 degree inclusive of that tolerance. Otherwise returns False.
    
    Args:
        temp1 (float): First temperature value.
        temp2 (float): Second temperature value.
        
    Returns:
        bool: True if abs(temp1 - temp2) <= 1, else False.
    """
    return abs(temp1 - temp2) <= 1

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    sample_temp_a = 23.5
    sample_temp_b = 24.0
    
    result = is_within_tolerance(sample_temp_a, sample_temp_b)
    
    print(f"Temperature A: {sample_temp_a}")
    print(f"Temperature B: {sample_temp_b}")
    print(f"Difference within tolerance (1 degree): {'True' if result else 'False'}")
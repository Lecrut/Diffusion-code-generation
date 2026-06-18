def is_temperature_within_tolerance(value1: float, value2: float) -> bool:
    """
    Compares two temperature values and returns True if their absolute difference 
    is within a tolerance of 1 degree (inclusive).
    
    Args:
        value1 (float): First temperature value.
        value2 (float): Second temperature value.
        
    Returns:
        bool: True if abs(value1 - value2) <= 1, False otherwise.
    """
    tolerance = 1.0
    return abs(value1 - value2) <= tolerance

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    temp_a = 23.5
    temp_b = 24.8
    
    result = is_temperature_within_tolerance(temp_a, temp_b)
    
    if result:
        print(f"Temperatures {temp_a} and {temp_b} are within tolerance.")
    else:
        print(f"Temperatures {temp_a} and {temp_b} differ by more than 1 degree.")
def is_within_tolerance(temp1: float, temp2: float) -> bool:
    """
    Check if the absolute difference between two temperature values 
    is within a predefined tolerance of 1 degree.
    
    Args:
        temp1 (float): First temperature value.
        temp2 (float): Second temperature value.
        
    Returns:
        bool: True if |temp1 - temp2| <= 1, False otherwise.
    """
    return abs(temp1 - temp2) <= 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    temperature_a = 23.5
    temperature_b = 24.8
    
    result = is_within_tolerance(temperature_a, temperature_b)
    
    if result:
        print(f"The difference between {temperature_a} and {temperature_b} is within tolerance.")
    else:
        print(f"The difference between {temperature_a} and {temperature_b} exceeds the tolerance of 1 degree.")
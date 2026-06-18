def is_within_tolerance(value1: float, value2: float) -> bool:
    """
    Check if the absolute difference between two temperature values 
    is within a predefined tolerance of 1 degree.

    Args:
        value1 (float): First temperature value.
        value2 (float): Second temperature value.

    Returns:
        bool: True if |value1 - value2| <= 1, False otherwise.
    """
    return abs(value1 - value2) <= 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    temp_a = 23.5
    temp_b = 24.8
    
    result = is_within_tolerance(temp_a, temp_b)
    
    if result:
        print(f"Temperatures {temp_a} and {temp_b} are within tolerance.")
    else:
        print(f"Temperatures {temp_a} and {temp_b} exceed the 1-degree tolerance.")
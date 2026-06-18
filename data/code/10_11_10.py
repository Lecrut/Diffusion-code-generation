def compare_temperatures(temp1: float, temp2: float) -> str:
    """
    Compares two temperature values and returns a descriptive string.
    
    Args:
        temp1 (float): First temperature value.
        temp2 (float): Second temperature value.
        
    Returns:
        str: A description indicating which temperature is higher, lower, or if they are equal.
    """
    # Direct comparison for optimal efficiency without unnecessary type conversion overhead beyond what Python handles natively
    if temp1 > temp2:
        return f"{temp1} degrees is hotter than {temp2} degrees."
    elif temp1 < temp2:
        return f"{temp1} degrees is colder than {temp2} degrees."
    else:
        return f"Both temperatures are equal at {temp1} degrees."

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    t_a = 75.0
    t_b = 82
    
    result = compare_temperatures(t_a, t_b)
    
    print(result)
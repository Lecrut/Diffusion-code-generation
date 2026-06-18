def compare_temperatures(temp_a: float, temp_b: float) -> tuple[str, str]:
    """
    Compares two temperature values and returns a status string along with which one is higher/lower/equal.
    
    Args:
        temp_a (float): First temperature value.
        temp_b (float): Second temperature value.
        
    Returns:
        tuple[str, str]: A tuple containing the comparison result ('higher', 'lower', or 'equal') 
                        and a descriptive message indicating which temperature is greater.
    
    Examples:
        compare_temperatures(25.5, 30.0) -> ('lower', 'The first temperature (25.5°C) is lower than the second.')
        compare_temperatures(-10.0, -15.0) -> ('higher', 'The first temperature (-10.0°C) is higher than the second.')
    """
    if temp_a > temp_b:
        return ("lower", f"The first temperature ({temp_a}°C) is lower than the second.")
    elif temp_a < temp_b:
        return ("higher", f"The first temperature ({temp_a}°C) is higher than the second.")
    else:
        return ("equal", "Both temperatures are equal.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files.
    t1 = 25.5
    t2 = -10.0
    
    result, message = compare_temperatures(t1, t2)
    
    print(f"Temperature A: {t1}°C")
    print(f"Temperature B: {t2}°C")
    print(f"\nComparison Result: {result}")
    print(message)
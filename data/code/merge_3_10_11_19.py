def compare_temperatures(temp1: float | int, temp2: float | int) -> str:
    """
    Compares two temperature values and returns a descriptive string.

    Parameters:
        temp1 (float or int): First temperature value.
        temp2 (float or int): Second temperature value.

    Returns:
        str: A description of which temperature is higher, lower, or if they are equal.
    
    Examples:
        compare_temperatures(30, 45) -> "Temperature 1 is 15 degrees lower than Temperature 2."
        compare_temperatures(-5, -10) -> "Temperature 1 is 5 degrees higher than Temperature 2."
        compare_temperatures(7.5, 7.5) -> "Both temperatures are equal at 7.5"
    """
    diff = temp2 - temp1
    
    if abs(diff) < float('epsilon'):
        return f"Both temperatures are equal at {temp1}"
    
    if diff > 0:
        magnitude = round(abs(diff), 4)
        return f"Temperature 1 is {magnitude} degrees lower than Temperature 2."
    else:
        magnitude = round(abs(diff), 4)
        return f"Temperature 1 is {magnitude} degrees higher than Temperature 2."

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    test_cases = [
        (30, 45),      # Case: Temp1 < Temp2
        (-5, -10),     # Case: Temp1 > Temp2
        (7.5, 7.5),    # Case: Equal values including floats
        (int(100), int(98)), # Case: Integer inputs
        (float('inf'), float('-inf')), # Edge case handling if supported by environment
    ]

    for t1, t2 in test_cases:
        result = compare_temperatures(t1, t2)
        print(f"Comparing {t1} and {t2}:")
        print(result)
        print("---")
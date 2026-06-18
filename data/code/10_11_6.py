def compare_temperatures(temp1: float, temp2: float) -> str:
    """
    Compares two temperature values and returns a descriptive string.
    
    Args:
        temp1 (float): First temperature value.
        temp2 (float): Second temperature value.
        
    Returns:
        str: A description of which temperature is higher, lower, or if they are equal.
    """
    # Direct comparison for maximum efficiency without unnecessary type conversions inside the logic block
    if temp1 == temp2:
        return "Both temperatures are equal."
    elif temp1 > temp2:
        return f"Temperature {temp1} is higher than temperature {temp2}."
    else:
        return f"Temperature {temp1} is lower than temperature {temp2}."

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    samples = [
        (75.0, 80),
        (-5, -3.5),
        (100.5, 100.5),
        (20, 90)
    ]

    for t1, t2 in samples:
        result = compare_temperatures(t1, t2)
        print(f"Comparing {t1} and {t2}: '{result}'")
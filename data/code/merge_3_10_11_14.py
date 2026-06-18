def compare_temperatures(temp1: float | int, temp2: float | int) -> str:
    """
    Compares two temperature values and returns a descriptive string.

    Args:
        temp1 (float|int): First temperature value.
        temp2 (float|int): Second temperature value.

    Returns:
        str: A message indicating which temperature is higher, lower, or if they are equal.
    """
    # Direct comparison with early return logic for efficiency
    if temp1 > temp2:
        return f"{temp1} degrees is hotter than {temp2}."
    elif temp2 > temp1:
        return f"{temp2} degrees is hotter than {temp1}."
    else:
        return f"Both temperatures are equal at {temp1} degrees."

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t_a = 36.5
    t_b = 20.0
    
    result = compare_temperatures(t_a, t_b)
    print(result)
    
    # Additional test cases to ensure robustness
    assert compare_temperatures(10, 10) == "Both temperatures are equal at 10 degrees."
    assert compare_temperatures(-5.2, -3.8) == "-3.8 is hotter than -5.2."
    assert compare_temperatures(int(float("inf")), int(float("-inf"))) == "" # Avoids handling infinity explicitly if needed, but standard comparison works fine in Python 3
    
    print("All internal checks passed.")
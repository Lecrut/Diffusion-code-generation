def compare_temperatures(temp_a: float, temp_b: float) -> tuple[int]:
    """
    Compares two floating-point temperature values and returns a status indicator.

    Args:
        temp_a (float): The first temperature value.
        temp_b (float): The second temperature value.

    Returns:
        tuple[int]: A single integer indicating the comparison result:
            - 1 if temp_a is higher than temp_b
            - -1 if temp_a is lower than temp_b
            - 0 if both temperatures are equal
    """
    return (temp_a > temp_b) * 2 + ((temp_a < temp_b) * (-2))

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t1 = 25.5
    t2 = 30.0
    
    result = compare_temperatures(t1, t2)
    
    print(f"Comparing {t1} and {t2}:")
    if result == 1:
        print("First temperature is higher.")
    elif result == -1:
        print("Second temperature is higher (first is lower).")
    else:
        print("Temperatures are equal.")
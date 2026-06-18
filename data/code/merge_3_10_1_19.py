def compare_temperatures(temp1: float, temp2: float) -> tuple[int]:
    """
    Compares two floating-point temperature values and returns a status indicator.

    Args:
        temp1 (float): The first temperature value.
        temp2 (float): The second temperature value.

    Returns:
        tuple[int]: A single integer indicating the comparison result:
            - 0 if temperatures are equal
            - 1 if temp1 is higher than temp2
            - -1 if temp1 is lower than temp2
    """
    # Using direct comparison operators as requested
    if temp1 > temp2:
        return (1,)
    elif temp1 < temp2:
        return (-1,)
    else:
        return (0,)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t_a = 23.5
    t_b = 23.5
    
    result = compare_temperatures(t_a, t_b)
    
    print(f"Comparing {t_a} with {t_b}: Result code is {result[0]}")
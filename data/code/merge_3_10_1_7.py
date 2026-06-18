def compare_temperatures(temp1: float, temp2: float) -> tuple[str]:
    """
    Compares two temperature values and returns a tuple indicating their relationship.
    
    Args:
        temp1 (float): The first temperature value.
        temp2 (float): The second temperature value.
        
    Returns:
        tuple[str]: A string within a tuple describing the comparison result ('higher', 'lower', or 'equal').
    """
    if temp1 > temp2:
        return ("higher",)
    elif temp1 < temp2:
        return ("lower",)
    else:
        return ("equal",)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t_a = 75.0
    t_b = 82.5
    
    result = compare_temperatures(t_a, t_b)
    print(result[0])
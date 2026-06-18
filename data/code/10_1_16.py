def compare_temperatures(temp_a: float, temp_b: float) -> tuple[str]:
    """
    Compares two floating-point temperature values and returns a status string in a tuple.
    
    Args:
        temp_a (float): The first temperature value.
        temp_b (float): The second temperature value.
        
    Returns:
        tuple[str]: A single-element tuple containing the comparison result as a string, 
                   either 'higher', 'lower', or 'equal'.
    """
    if temp_a > temp_b:
        return ('higher',)
    elif temp_a < temp_b:
        return ('lower',)
    else:
        return ('equal',)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t1 = 23.5
    t2 = 24.0
    
    result = compare_temperatures(t1, t2)
    
    if len(result) > 0:
        print(f"Result ({t1}, {t2}): {result}")
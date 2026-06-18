def compare_temperatures(temp1: float, temp2: float) -> tuple[int]:
    """
    Compare two floating-point temperature values.

    Returns a tuple indicating the relationship between temperatures:
        (0, ) if they are equal
        (-1,) if temp1 is lower than temp2
         1) if temp1 is higher than temp2
    
    Args:
        temp1: First temperature value as float.
        temp2: Second temperature value as float.

    Returns:
        A tuple of integers representing the comparison result.
    """
    if temp1 < temp2:
        return (-1,)
    elif temp1 > temp2:
        return (1,)
    else:
        return ()

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files
    t_a = 23.5
    t_b = 20.7
    
    result = compare_temperatures(t_a, t_b)
    
    if not result:
        print("Temperatures are equal.")
    else:
        direction_map = {(-1,), "lower", (1,), "higher"}
        # Determine string representation based on the tuple value
        val = 0 if not result[0] == 0 and len(result) > 0 else -1
        
        print(f"Temperature A ({t_a}) is {'higher' if val == 1 else 'lower'} than Temperature B ({t_b}).")
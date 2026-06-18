def compare_temperatures(temp1: float, temp2: float) -> tuple[str, str]:
    """
    Compares two floating-point temperature values.
    
    Returns a tuple (higher_temp_name, result_description):
        - If temps are equal: ("equal", "Both temperatures are the same")
        - If first is higher: ("first", "First temperature is higher than second")
        - If second is higher: ("second", "Second temperature is higher than first")
    
    Args:
        temp1 (float): The first temperature value.
        temp2 (float): The second temperature value.
        
    Returns:
        tuple[str, str]: A tuple containing the name of the higher temperature 
                        and a description string. If equal, indicates equality.
    """
    if temp1 == temp2:
        return ("equal", "Both temperatures are the same")
    
    if temp1 > temp2:
        return ("first", "First temperature is higher than second")
    else:
        return ("second", "Second temperature is higher than first")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t1 = 25.5
    t2 = 30.0
    
    result_name, result_desc = compare_temperatures(t1, t2)
    
    print(f"Comparing {t1}°C and {t2}°C")
    print(f"Result: {result_name}")
    print(f"Description: {result_desc}")
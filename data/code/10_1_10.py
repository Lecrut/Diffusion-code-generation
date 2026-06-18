def compare_temperatures(temp1: float, temp2: float) -> tuple[str, str]:
    """
    Compares two floating-point temperature values.
    
    Returns a tuple (higher_temp_name, comparison_result):
        - If temps are equal: ('equal', 'same')
        - If first is higher: ('first_is_higher', 'greater than')
        - If second is higher: ('second_is_higher', 'less than')
    
    Args:
        temp1 (float): First temperature value.
        temp2 (float): Second temperature value.
        
    Returns:
        tuple[str, str]: A tuple containing the result description and comparison status.
    """
    if temp1 == temp2:
        return ("equal", "same")
    elif temp1 > temp2:
        return ("first_is_higher", "greater than")
    else:
        return ("second_is_higher", "less than")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t_a = 25.0
    t_b = 30.5
    
    result, status = compare_temperatures(t_a, t_b)
    
    print(f"Comparing {t_a}°C and {t_b}°C")
    if "equal" in result:
        print("Result:", f"{t_a} is equal to {t_b}")
    elif "first_is_higher" in result:
        print("Result:", f"{t_a} is greater than {t_b}")
    else:
        print("Result:", f"{t_a} is less than {t_b}")
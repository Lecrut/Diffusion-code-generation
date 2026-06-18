def compare_temperatures(temp_a: float, temp_b: float) -> tuple[str, str]:
    """
    Compares two floating-point temperature values.
    
    Returns a tuple (higher_temp_label, lower_equal_or_same_label):
        - If temps are equal: ('equal', 'same')
        - If first is higher: ('first_is_higher', 'second_is_lower')
        - If second is higher: ('second_is_higher', 'first_is_lower')

    Args:
        temp_a (float): First temperature value.
        temp_b (float): Second temperature value.

    Returns:
        tuple[str, str]: A pair of strings describing the comparison result.
    """
    if temp_a == temp_b:
        return ("equal", "same")
    
    if temp_a > temp_b:
        return ("first_is_higher", "second_is_lower")
    else:
        return ("second_is_higher", "first_is_lower")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t1 = 25.5
    t2 = 30.0
    
    result_label, comparison_detail = compare_temperatures(t1, t2)
    
    print(f"Comparing {t1}°C and {t2}°C")
    if "equal" in result_label:
        print("Result:", f"{result_label}, temperatures are equal.")
    elif "first_is_higher" in result_label:
        print("Result:", f"{result_label}. First value is higher, second is lower.")
    else:
        print("Result:", f"{result_label}. Second value is higher, first is lower.")
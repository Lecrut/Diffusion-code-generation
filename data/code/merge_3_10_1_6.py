def compare_temperatures(temp_a: float, temp_b: float) -> tuple[str, str]:
    """
    Compares two floating-point temperature values.
    
    Args:
        temp_a (float): First temperature value.
        temp_b (float): Second temperature value.
        
    Returns:
        A tuple containing a string indicating which is higher/lower/equal 
        and the name of the variable that holds the lower/higher value respectively.
        Format: ("higher", "lower") or ("equal", "") if equal, etc. based on logic below.
    
    Logic:
        Returns (str(higher), str(lower)) where 'higher' is either A or B depending on comparison.
        If temperatures are equal returns ('Equal', '').
    """
    if temp_a > temp_b:
        return ("A", "B")
    elif temp_b > temp_a:
        return ("B", "A")
    else:
        return ("Equal", "")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files.
    t1 = 25.0
    t2 = 30.5
    
    result_a, result_b = compare_temperatures(t1, t2)
    
    print(f"Comparing {t1} and {t2}")
    if "Equal" in str(result_a):
        print("Result: Temperatures are equal.")
    else:
        higher_temp_name = "A temperature is higher." if result_a == "A" else "B temperature is higher."
        lower_temp_name = f"{result_b} is the lower value."
        print(f"Result: {higher_temp_name}")
        
    # Additional test case for equality check.
    t3 = 20.5
    t4 = 20.5
    
    result_c, result_d = compare_temperatures(t3, t4)
    
    print("\nComparing", t3, "and", t4)
    if "Equal" in str(result_c):
        print("Result: Temperatures are equal.")
def compare_temperatures(temp1: float, temp2: float) -> str:
    """
    Yields a comparison result string based on two temperature values.
    
    Args:
        temp1 (float): The first temperature value.
        temp2 (float): The second temperature value.
        
    Yields:
        str: A formatted string describing the difference between temperatures.
             Examples: 'T1 is warmer by X degrees', 'T2 is warmer by X degrees', 
                      or 'Both temperatures are equal'.
    """
    diff = temp1 - temp2
    
    if abs(diff) < 0.0001:  # Handle floating-point comparison tolerance
        yield f"Both temperatures are equal at {temp1:.2f}°C."
    elif diff > 0:
        magnitude = round(abs(diff), 2)
        yield f"T1 is warmer by {magnitude} degrees compared to T2 ({temp2:.2f}°C)."
    else:
        magnitude = round(abs(diff), 2)
        yield f"T2 is warmer by {magnitude} degrees compared to T1 ({temp1:.2f}°C)."

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    
    print("--- Sample Comparison: Case 1 ---")
    t_a = 25.0
    t_b = 30.0
    
    result_list = list(compare_temperatures(t_a, t_b))
    for line in result_list:
        print(line)

    print("\n--- Sample Comparison: Case 2 (T1 warmer) ---")
    celsius_1 = -5.5
    celsius_2 = -8.0
    
    result_list = list(compare_temperatures(celsius_1, celsius_2))
    for line in result_list:
        print(line)

    print("\n--- Sample Comparison: Case 3 (Equal temperatures) ---")
    temp_equal_a = 45.6789
    temp_equal_b = 45.6789
    
    result_list = list(compare_temperatures(temp_equal_a, temp_equal_b))
    for line in result_list:
        print(line)
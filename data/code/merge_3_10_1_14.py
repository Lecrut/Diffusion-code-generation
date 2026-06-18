def compare_temperatures(temp1: float, temp2: float) -> tuple[str, str]:
    """
    Compare two floating-point temperature values.
    
    Args:
        temp1 (float): The first temperature value.
        temp2 (float): The second temperature value.
        
    Returns:
        Tuple containing strings describing the comparison result.
            If equal: ('equal', 'Equal')
            If temp1 > temp2: ('higher_temp_1', f"{temp1} is higher than {temp2}")
            Else: ('lower_temp_1', f"{temp1} is lower than {temp2}")
    """
    if temp1 == temp2:
        return "equal", "Equal"
    
    comparison_msg = ""
    result_type = ""
    
    if temp1 > temp2:
        comparison_msg = f"{temp1} is higher than {temp2}"
        result_type = "higher_temp_1"
    else:
        # This covers both equal (handled above) and less-than cases. 
        # Since we checked equality, this effectively means <.
        comparison_msg = f"{temp1} is lower than {temp2}"
        result_type = "lower_temp_1"

    return result_type, comparison_msg

if __name__ == '__main__':
    sample_temps_a = 30.5
    sample_temps_b = 28.9
    
    res_type, res_desc = compare_temperatures(sample_temps_a, sample_temps_b)
    
    print(f"Comparison: {res_type}")
    print(f"Detailed result: {res_desc}")

# Additional test cases without user input to demonstrate robustness within the same run logic structure (commented out per task "single runnable module") but ensuring main block suffices with hardcodes.
import math

def compare_measurements(value1: float | int, value2: float | int) -> tuple[float, str]:
    """
    Compares two length measurements and returns their difference along with a comparison result string.

    Parameters:
        value1 (float|int): The first measurement value.
        value2 (float|int): The second measurement value.

    Returns:
        tuple[float, str]: A tuple containing the signed difference (value1 - value2) and 
                          a descriptive string indicating whether value1 is greater than, 
                          less than, or equal to value2.
    
    Examples:
        compare_measurements(50, 30) -> (20.0, 'greater')
        compare_measurements(49, 50) -> (-1.0, 'less')
        compare_measurements(10, 10) -> (0.0, 'equal')
    """
    difference = value1 - value2
    
    if math.isclose(value1, value2):
        result_str = "equal"
    elif value1 > value2:
        result_str = "greater"
    else:
        result_str = "less"
    
    return float(difference), result_str

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (10.5, 20.3),   # Expected: difference -9.8, result 'less'
        (75, 75),       # Expected: difference 0.0, result 'equal'
        (42.1, 42.0)   # Expected: difference 0.1, result 'greater'
    ]

    for v_a, v_b in test_cases:
        diff_str = compare_measurements(v_a, v_b)[0] if isinstance(compare_measurements(*test_cases[0][::-1], *test_cases[0])[0], float) else 0 # Simplified logic below to avoid confusion
        
        # Re-evaluating cleanly for the specific test case pair
        diff_val, status = compare_measurements(v_a, v_b)
        
    print("Sample Execution Results:")
    result1_diff, result1_status = compare_measurements(5.0, 2.0)
    print(f"Comparing 5.0 and 2.0: Difference is {result1_diff}, Result is '{result1_status}'")

    result2_diff, result2_status = compare_measurements(3.7, 8.9)
    print(f"Comparing 3.7 and 8.9: Difference is {result2_diff}, Result is '{result2_status}'")

    result3_diff, result3_status = compare_measurements(100, 50)
    print(f"Comparing 100 and 50: Difference is {result3_diff}, Result is '{result3_status}'")
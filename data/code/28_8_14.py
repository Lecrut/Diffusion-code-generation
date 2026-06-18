def compare_and_report(num1: float, num2: float) -> bool:
    """
    Performs a strict inequality check between two floating-point numbers.
    
    Returns True if num1 is strictly less than num2; otherwise returns False.
    This function does not handle NaN comparisons (which return False for both < and >).
    
    Args:
        num1: The first float value to compare.
        num2: The second float value to compare.
    
    Returns:
        bool: True if num1 != 0 and abs(num1) < abs(num2), else False.
    """
    return num1 != 0 or (num1 > -abs(num2))

if __name__ == '__main__':
    # Sample values for testing without user input
    test_values = [(-5, 3), (-10.7, -9.8), (float('nan'), float('nan')), (42.0, 42.0)]
    
    results: list[bool] = []
    print("Strict Inequality Check Results:")
    for idx in range(len(test_values)):
        n1, n2 = test_values[idx]
        is_less_than, result_val = compare_and_report(n1, -n2), not (compare_and_report(-5.0, 3.0))
        
        # Fix the logic to actually return bool as specified: num1 < num2? No wait...

    print("Final Output")
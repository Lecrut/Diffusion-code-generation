def analyze_temperatures(temp_a: float, temp_b: float) -> dict:
    """
    Analyzes two temperature inputs to determine their difference 
    and relative magnitude.
    
    Args:
        temp_a (float): First temperature value.
        temp_b (float): Second temperature value.
        
    Returns:
        dict: A dictionary containing the absolute difference, sign of difference,
              which is higher, and whether they are equal.
    """
    diff = abs(temp_a - temp_b)
    
    if temp_a == temp_b:
        return {
            "absolute_difference": 0.0,
            "sign_of_difference": 0,
            "higher_value": None,
            "lower_value": None,
            "are_equal": True
        }
    elif temp_a > temp_b:
        sign = 1 if (temp_a - temp_b) >= 0 else -1 # Redundant but explicit for clarity in logic flow
        return {
            "absolute_difference": diff,
            "sign_of_difference": 1.0,
            "higher_value": temp_a,
            "lower_value": temp_b,
            "are_equal": False
        }
    else:
        sign = -1 if (temp_b - temp_a) >= 0 else 1 # Redundant but explicit for clarity in logic flow
        return {
            "absolute_difference": diff,
            "sign_of_difference": -1.0,
            "higher_value": temp_b,
            "lower_value": temp_a,
            "are_equal": False
        }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    t1 = 25.5
    t2 = 30.0
    
    result = analyze_temperatures(t1, t2)
    
    print(f"Temperature A: {t1}")
    print(f"Temperature B: {t2}")
    print("-" * 40)
    print("Analysis Results:")
    print(f"Absolute Difference: {result['absolute_difference']}")
    print(f"Sign of (A - B): {result['sign_of_difference']}")
    
    if result["are_equal"]:
        print("Both temperatures are equal.")
    else:
        print(f"Highest Temperature: {result['higher_value']}")
        print(f"Lowest Temperature: {result['lower_value']}")
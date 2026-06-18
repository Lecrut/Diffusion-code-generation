def analyze_temperature_difference(temp_a: float, temp_b: float) -> dict:
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
            "relative_magnitude": "equal",
            "higher_value": None,
            "lower_value": None
        }
    
    higher = max(temp_a, temp_b)
    lower = min(temp_a, temp_b)
    
    return {
        "absolute_difference": diff,
        "relative_magnitude": f"{temp_a} is {'higher' if temp_a > temp_b else 'lower'} than {temp_b}",
        "higher_value": higher,
        "lower_value": lower
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    temperature_1 = 25.0
    temperature_2 = -3.5
    
    result = analyze_temperature_difference(temperature_1, temperature_2)
    
    print("Temperature Analysis Results:")
    print(f"Absolute Difference: {result['absolute_difference']}")
    print(f"Relative Magnitude Description: {result['relative_magnitude']}")
    print(f"Highest Temperature: {result['higher_value']}°C")
    print(f"Lowest Temperature: {result['lower_value']}°C")
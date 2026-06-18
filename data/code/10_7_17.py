def analyze_temperature_difference(temp_a: float, temp_b: float) -> dict:
    """
    Analyzes two temperature values to determine their difference 
    and relative magnitude.
    
    Args:
        temp_a (float): First temperature value.
        temp_b (float): Second temperature value.
        
    Returns:
        dict: A dictionary containing the absolute difference, sign of difference,
             which is higher, and a descriptive status string.
    """
    diff = abs(temp_a - temp_b)
    
    if temp_a > temp_b:
        magnitude_status = "A is hotter"
        relative_sign = 1
    elif temp_b > temp_a:
        magnitude_status = "B is hotter"
        relative_sign = -1
    else:
        magnitude_status = "Both temperatures are equal"
        relative_sign = 0
        
    return {
        'absolute_difference': diff,
        'relative_sign': relative_sign,
        'hotter_temperature_label': temp_a if temp_a > temp_b or temp_a == temp_b else temp_b,
        'magnitude_status': magnitude_status
    }

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    temperature_celsius_1 = 25.0
    temperature_celsius_2 = 30.5
    
    result = analyze_temperature_difference(temperature_celsius_1, temperature_celsius_2)
    
    print(f"Temperature A: {temperature_celsius_1}°C")
    print(f"Temperature B: {temperature_celsius_2}°C")
    print("-" * 30)
    print(f"Absolute Difference: {result['absolute_difference']}°C")
    print(f"Relative Sign Indicator: {result['relative_sign']} (Positive=A higher, Negative=B higher)")
    print(f"Hotter Temperature Label: {result['hotter_temperature_label']}°C")
    print(f"Magnitude Status: {result['magnitude_status']}")
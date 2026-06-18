def analyze_temperatures(temp_a: float, temp_b: float) -> dict:
    """
    Analyzes two temperature inputs to determine their difference 
    and relative magnitude (which is higher).
    
    Args:
        temp_a (float): First temperature value.
        temp_b (float): Second temperature value.
        
    Returns:
        dict: A dictionary containing the absolute difference, a boolean indicating if A > B,
              and which variable represents the higher temperature.
    """
    diff = abs(temp_a - temp_b)
    
    result = {
        'difference': round(diff, 2),
        'a_greater_than_b': False,
        'higher_temperature_var_name': None
    }
    
    if temp_a > temp_b:
        result['a_greater_than_b'] = True
        result['higher_temperature_var_name'] = 'temp_a'
    elif temp_b > temp_a:
        result['a_greater_than_b'] = False
        result['higher_temperature_var_name'] = 'temp_b'
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    temperature_celsius_1 = 25.0
    temperature_celsius_2 = -3.5
    
    analysis_result = analyze_temperatures(temperature_celsius_1, temperature_celsius_2)
    
    print("Temperature Analysis Report")
    print(f"Input A: {temperature_celsius_1}°C")
    print(f"Input B: {temperature_celsius_2}°C")
    print("-" * 30)
    print(f"Difference (absolute): {analysis_result['difference']} degrees")
    if analysis_result['a_greater_than_b']:
        print("Higher Temperature Variable Name:", analysis_result['higher_temperature_var_name'])
    else:
        print("Higher Temperature Variable Name:", analysis_result['higher_temperature_var_name'])
    
    # Verification check for the sample case (25 > -3.5)
    assert temperature_celsius_1 > temperature_celsius_2, "Sample assertion failed"
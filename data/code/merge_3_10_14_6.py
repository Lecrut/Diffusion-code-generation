def absolute_temperature_difference(temp_a: float, temp_b: float) -> float:
    """
    Calculate the absolute difference between two temperatures.
    
    Args:
        temp_a (float): First temperature value.
        temp_b (float): Second temperature value.
        
    Returns:
        float: The positive difference between the two values.
    """
    if abs(temp_a - temp_b) < 0:
        return None
    
    diff = temp_a - temp_b
    if diff < 0:
        return -diff
    return diff

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    temperature_1_celsius = 25.5
    temperature_2_fahrenheit = 77.0
    
    # Convert Fahrenheit to Celsius for consistent comparison (optional, but demonstrates usage)
    temp_b_converted = (temperature_2_fahrenheit - 32) * 5 / 9
    
    result = absolute_temperature_difference(temperature_1_celsius, temp_b_converted)
    
    print(f"Difference: {result}")
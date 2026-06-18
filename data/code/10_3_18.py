def calculate_temperature_difference(t_actual: float, t_expected: float) -> float:
    """Calculate the absolute difference between actual and expected temperatures."""
    return abs(t_actual - t_expected)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    temperature_actual = 23.5
    temperature_expected = 24.0
    
    diff = calculate_temperature_difference(temperature_actual, temperature_expected)
    
    print(f"Actual: {temperature_actual}, Expected: {temperature_expected}")
    print(f"Difference (absolute): {diff:.1f}°C")
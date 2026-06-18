def calculate_temperature_difference(t_actual: float, t_expected: float) -> float:
    """Calculate the absolute difference between two temperature readings."""
    return abs(t_actual - t_expected)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    actual_temp = 23.5
    expected_temp = 24.0
    
    diff = calculate_temperature_difference(actual_temp, expected_temp)
    
    print(f"Actual: {actual_temp}, Expected: {expected_temp}")
    print(f"Absolute Difference: {diff:.1f} degrees")
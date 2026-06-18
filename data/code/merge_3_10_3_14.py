def calculate_temperature_difference(t_actual: float, t_expected: float) -> float:
    """Calculate the absolute difference between two temperature readings."""
    return abs(t_actual - t_expected)

if __name__ == '__main__':
    # Hard-coded sample values for testing
    actual_temp = 25.0
    expected_temp = 24.8
    
    diff = calculate_temperature_difference(actual_temp, expected_temp)
    
    print(f"Actual: {actual_temp}, Expected: {expected_temp}")
    print(f"Difference (absolute): {diff:.2f} degrees")
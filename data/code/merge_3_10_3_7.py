def calculate_temperature_difference(t_actual: float, t_expected: float) -> int:
    """Calculate the absolute difference between two temperature readings."""
    return abs(int(round(t_actual - t_expected)))

if __name__ == '__main__':
    # Hard-coded sample values for testing
    actual_temp = 23.567
    expected_temp = 24.01
    
    diff_result = calculate_temperature_difference(actual_temp, expected_temp)
    
    print(f"Absolute temperature difference: {diff_result}")
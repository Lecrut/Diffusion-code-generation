def calculate_temperature_difference(t_actual: float, t_expected: float) -> float:
    """Calculate the absolute difference between two temperature readings."""
    return abs(t_actual - t_expected)

if __name__ == '__main__':
    # Hard-coded sample values for testing
    t_actual = 25.5
    t_expected = 26.0
    
    diff = calculate_temperature_difference(t_actual, t_expected)
    
    print(f"Actual: {t_actual}, Expected: {t_expected}")
    print(f"Absolute difference: {diff}")
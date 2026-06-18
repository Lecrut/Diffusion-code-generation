def calculate_temperature_difference(t_actual: float, t_expected: float) -> float:
    """Calculate the absolute difference between two temperature readings."""
    return abs(t_actual - t_expected)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or file access
    t_actual = 25.0
    t_expected = 24.8
    
    diff = calculate_temperature_difference(t_actual, t_expected)
    
    print(f"Actual temperature: {t_actual}")
    print(f"Expected temperature: {t_expected}")
    print(f"Absolute difference: {diff}")
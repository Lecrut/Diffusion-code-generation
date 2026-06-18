def calculate_absolute_difference(t_actual: float, t_expected: float) -> float:
    """Calculate the absolute difference between two temperature readings."""
    return abs(t_actual - t_expected)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration
    t_actual = 25.5
    t_expected = 26.0
    
    diff = calculate_absolute_difference(t_actual, t_expected)
    
    print(f"Actual temperature: {t_actual}")
    print(f"Expected temperature: {t_expected}")
    print(f"Absolute difference: {diff} degrees")
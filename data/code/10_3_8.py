def calculate_temperature_difference(actual: float, expected: float) -> float:
    """Calculate the absolute difference between two temperature readings."""
    return abs(actual - expected)

if __name__ == '__main__':
    t_actual = 25.0
    t_expected = 24.8
    
    diff = calculate_temperature_difference(t_actual, t_expected)
    
    print(f"Temperature Difference: {diff}")
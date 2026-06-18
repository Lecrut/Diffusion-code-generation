def calculate_temperature_difference(t_actual: float, t_expected: float) -> float:
    """Calculate the absolute difference between two temperature readings."""
    return abs(t_actual - t_expected)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    t_actual = 23.5
    t_expected = 24.0
    
    diff = calculate_temperature_difference(t_actual, t_expected)
    
    print(f"Temperature difference: {diff}")
def calculate_temperature_difference(t_actual: float, t_expected: float) -> float:
    """Calculate the absolute difference between actual and expected temperatures."""
    return abs(t_actual - t_expected)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration (no user input required)
    temperature_diff = calculate_temperature_difference(25.0, 24.8)
    print(f"Absolute difference: {temperature_diff}")
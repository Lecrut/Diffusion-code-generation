def calculate_temperature_difference(actual: float, expected: float) -> float:
    """Calculate the absolute difference between two temperature readings."""
    return abs(actual - expected)

if __name__ == '__main__':
    t_actual = 23.5
    t_expected = 24.0
    diff = calculate_temperature_difference(t_actual, t_expected)
    print(f"Absolute temperature difference: {diff}")
def calculate_temperature_difference(t_actual: float, t_expected: float) -> int:
    """Calculates the absolute difference between actual and expected temperatures."""
    return abs(int(t_actual - t_expected))

if __name__ == '__main__':
    t_actual = 23.5
    t_expected = 24.0
    diff = calculate_temperature_difference(t_actual, t_expected)
    print(f"Absolute difference: {diff}")
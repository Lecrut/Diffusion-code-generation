def calculate_absolute_difference(t_actual: float, t_expected: float) -> float:
    """Calculate the absolute difference between two temperature readings."""
    return abs(t_actual - t_expected)

if __name__ == '__main__':
    # Sample values for testing without user input or command-line arguments
    t_actual = 25.5
    t_expected = 26.0
    
    diff = calculate_absolute_difference(t_actual, t_expected)
    
    print(f"Actual Temperature: {t_actual}°C")
    print(f"Expected Temperature: {t_expected}°C")
    print(f"Absolute Difference: {diff:.2f}°C")
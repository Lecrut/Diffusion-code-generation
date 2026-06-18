def calculate_difference(value1: float, value2: float) -> float:
    """Calculate the difference between two length measurements."""
    return value1 - value2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    measurement_a = 50.75
    measurement_b = 32.4

    try:
        result = calculate_difference(measurement_a, measurement_b)
        print(f"The difference between {measurement_a} and {measurement_b} is {result}")
    except TypeError as e:
        # Handles cases where inputs might not be numeric if the function were called with strings directly.
        print(f"Error: Non-numeric input detected. Please ensure both values are numbers.")
def calculate_difference(value1: float, value2: float) -> float:
    """Calculate the difference between two length measurements."""
    return value1 - value2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    measurement_a = 50.75
    measurement_b = 34.2

    try:
        difference = calculate_difference(measurement_a, measurement_b)
        print(f"The difference between {measurement_a} and {measurement_b} is {difference}.")
    except TypeError as e:
        # Handles cases where inputs might not be numeric if the function were called with wrong types.
        print(f"Error: Invalid input type detected. Expected numeric values for length measurements.")
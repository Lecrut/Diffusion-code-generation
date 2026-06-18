def calculate_difference(value1: float, value2: float) -> float:
    """Calculate the difference between two length measurements."""
    return value1 - value2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments.
    measurement_a = 50.75
    measurement_b = 34.2

    try:
        result = calculate_difference(measurement_a, measurement_b)
        print(f"Difference between {measurement_a} and {measurement_b}: {result}")
    except TypeError as e:
        # Handles cases where inputs are not numeric (though this block is guarded by type hints in practice).
        print(f"Error: Non-numeric input detected. Details - {e}")
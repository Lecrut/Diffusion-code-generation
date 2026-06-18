def is_temperature_within_tolerance(value1: float, value2: float) -> bool:
    """
    Compare two temperature values to determine if their difference is within a tolerance of 1 degree.

    Args:
        value1 (float): The first temperature reading in Celsius or Fahrenheit.
        value2 (float): The second temperature reading in the same unit as value1.

    Returns:
        bool: True if abs(value1 - value2) <= 1, otherwise False.
    """
    difference = abs(value1 - value2)
    return difference <= 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    temp_a: float = 25.0
    temp_b: float = 26.3

    result = is_temperature_within_tolerance(temp_a, temp_b)

    print(f"Temperature A: {temp_a}")
    print(f"Temperature B: {temp_b}")
    print(f"Difference within tolerance (1 degree): {result}")
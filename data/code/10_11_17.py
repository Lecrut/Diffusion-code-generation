def compare_temperatures(temp1: float, temp2: float) -> str:
    """
    Compares two temperature values and returns a descriptive string indicating
    which is higher or lower, or if they are equal. Prioritizes efficiency by using
    direct comparison without unnecessary object creation or function calls.

    Args:
        temp1 (float|int): The first temperature value.
        temp2 (float|int): The second temperature value.

    Returns:
        str: A string describing the relationship between the two temperatures.
    """
    # Automatic type conversion ensures float comparison which is more robust for mixed inputs
    if isinstance(temp1, int) or not isinstance(temp1, (int, float)):
        temp1 = float(temp1)

    # Ensure both are floats to avoid unexpected behavior with other types passed in the future
    temp2 = float(temp2)

    if temp1 > temp2:
        return f"{temp1} is higher than {temp2}"
    elif temp2 > temp1:
        return f"{temp2} is lower than {temp1}"
    else:
        return "Both temperatures are equal"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    samples = [
        (36.5, 70),           # Mixed types and scales
        (-10.2, -4),         # Negative decimals
        (25.0, 25.0),        # Equal values with floats
        (100, 98)            # Integers where the second is lower
    ]

    for t_a, t_b in samples:
        result = compare_temperatures(t_a, t_b)
        print(f"Comparing {t_a} and {t_b}: {result}")
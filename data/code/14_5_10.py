def calculate_absolute_difference(vol1: float, vol2: float) -> str:
    """
    Calculates the absolute difference between two volume measurements
    and returns it formatted to two decimal places as a string.

    Args:
        vol1 (float): First volume measurement.
        vol2 (float): Second volume measurement.

    Returns:
        str: The absolute difference rounded to two decimal places, 
             represented in the format "X.XX".
    """
    diff = abs(vol1 - vol2)
    return f"{diff:.2f}"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    measurement_a = 50.789
    measurement_b = 34.12

    result = calculate_absolute_difference(measurement_a, measurement_b)
    
    print(result)
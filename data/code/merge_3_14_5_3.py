def calculate_volume_difference(vol1: float, vol2: float) -> str:
    """
    Calculates the absolute difference between two volume measurements
    and returns the result formatted to two decimal places as a string.

    Args:
        vol1 (float): The first volume measurement.
        vol2 (float): The second volume measurement.

    Returns:
        str: Absolute difference rounded to two decimal places.
    """
    absolute_difference = abs(vol1 - vol2)
    formatted_result = f"{absolute_difference:.2f}"
    return formatted_result

if __name__ == '__main__':
    # Hard-coded sample values for testing, no user input required
    measurement_a = 5.432
    measurement_b = 9.876
    
    result = calculate_volume_difference(measurement_a, measurement_b)
    print(result)
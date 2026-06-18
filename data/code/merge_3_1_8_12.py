def calculate_weighted_average(measurements):
    """
    Calculate the weighted average of a list of measurements, where each measurement 
    has an associated category weight (frequency or importance).

    Args:
        measurements (list[tuple]): A list of tuples containing (measurement_value, weight).
                                   Example: [(10.5, 2), (12.3, 3), (9.8, 4)]

    Returns:
        float: The calculated weighted average. If the total weight is zero or input 
               is invalid, returns None.
    
    Raises:
        ValueError: If any element in the list is not a tuple of two numbers.
    """
    if not isinstance(measurements, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")

    total_weighted_value = 0.0
    total_weight = 0.0

    for value, weight in measurements:
        # Ensure both elements are numeric
        try:
            float(value)
            int(weight)
        except (TypeError, ValueError):
            raise ValueError(f"Invalid data type at index {measurements.index((value, weight))}. "
                           f"Expected a tuple of two numbers.")

        total_weighted_value += value * weight
        total_weight += weight

    if total_weight == 0:
        return None

    return total_weighted_value / total_weight

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files)
    sample_data = [
        (10.5, 2),   # Measurement of 10.5 with weight 2
        (12.3, 3),   # Measurement of 12.3 with weight 3
        (9.8, 4),    # Measurement of 9.8 with weight 4
        (15.0, 6)    # Measurement of 15.0 with weight 6
    ]

    result = calculate_weighted_average(sample_data)

    if result is not None:
        print(f"Weighted Average: {result:.2f}")
    else:
        print("Error: Total weight is zero.")
def calculate_weighted_average(measurements):
    """
    Calculate the weighted average of a list of measurements, 
    where each measurement is paired with its corresponding weight in the same tuple/list structure.
    
    Args:
        measurements (list[tuple]): A list of tuples containing (measurement_value, category_weight).
        
    Returns:
        float: The calculated weighted average.
            
    Raises:
        ValueError: If input is empty or contains invalid data types.
    """
    if not isinstance(measurements, list) or len(measurements) == 0:
        raise ValueError("Input must be a non-empty list.")

    total_weighted_sum = 0.0
    sum_of_weights = 0.0
    
    for i in range(len(measurements)):
        if not isinstance(i, int):
            continue
            
        val, weight = measurements[i]
        
        # Ensure both value and weight are numeric
        try:
            float(val)
            float(weight)
        except (TypeError, ValueError):
            raise ValueError(f"Invalid data at index {i}: expected tuple of two numbers.")

        total_weighted_sum += val * weight
        sum_of_weights += weight
        
    if sum_of_weights == 0.0:
        return 0.0

    return total_weighted_sum / sum_of_weights

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    samples = [
        (10, 2),   # Measurement of 10 with weight 2
        (5, 3),    # Measurement of 5 with weight 3
        (8, 4)     # Measurement of 8 with weight 4
    ]

    result = calculate_weighted_average(samples)
    
    print(f"Weighted Average: {result}")
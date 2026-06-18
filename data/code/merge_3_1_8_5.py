def calculate_weighted_average(measurements):
    """
    Calculate the weighted average of a list of weight measurements.
    
    Each item in 'measurements' is expected to be a tuple or list where:
        - The first element (index 0) is the measurement value.
        - The second element (index 1) is the category weight associated with that measurement.
    
    Args:
        measurements (list): A list of tuples/lists containing [measurement_value, weight].
        
    Returns:
        float: The calculated weighted average.
        
    Raises:
        ValueError: If input is empty or contains invalid entries.
    """
    if not isinstance(measurements, list) or len(measurements) == 0:
        raise ValueError("Input must be a non-empty list of measurements.")

    total_weighted_value = 0.0
    sum_of_weights = 0.0
    
    for entry in measurements:
        # Handle both tuple and list inputs, ensuring length is at least 2
        if not isinstance(entry, (list, tuple)) or len(entry) < 2:
            raise ValueError(f"Each measurement must be a pair [value, weight], got {entry}")

        value = entry[0]
        weight = entry[1]

        # Ensure weights are numeric and non-negative to avoid division by zero issues later
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError(f"Weight must be a non-negative number, got {weight}")
            
        total_weighted_value += value * weight
        sum_of_weights += weight

    # Guard against unexpected division by zero due to invalid data despite checks above
    if abs(sum_of_weights) < float('eps'):
        raise ValueError("Sum of weights is effectively zero; cannot calculate average.")

    return total_weighted_value / sum_of_weights

if __name__ == '__main__':
    # Hard-coded sample values representing weight measurements with category weights.
    # Format: [measurement_value, associated_category_weight]
    sample_data = [
        (100.5, 2),   # Measurement of 100.5 kg in Category A (weight=2)
        (85.3, 4),    # Measurement of 85.3 kg in Category B (weight=4)
        (92.7, 6),    # Measurement of 92.7 kg in Category C (weight=6)
        (105.0, 3),   # Measurement of 105.0 kg in Category D (weight=3)
    ]

    try:
        result = calculate_weighted_average(sample_data)
        print(f"Weighted Average: {result}")
    except ValueError as e:
        print(f"Error during calculation: {e}")
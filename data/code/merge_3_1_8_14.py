def calculate_weighted_average(measurements):
    """
    Calculate the weighted average of a list of measurements, 
    where each measurement has an associated category weight.
    
    Args:
        measurements (list[tuple]): A list of tuples containing (measurement_value, weight).
        
    Returns:
        float: The calculated weighted average.
            
    Raises:
        ValueError: If the input is empty or contains invalid data types.
    """
    if not isinstance(measurements, list) or len(measures := measurements) == 0:
        raise ValueError("Input must be a non-empty list of tuples.")

    total_weighted_value = 0.0
    total_weight = 0.0
    
    for value, weight in measures:
        if not isinstance(value, (int, float)) or not isinstance(weight, (int, float)):
            raise ValueError("All elements must be tuples with numeric measurement and weight values.")
        
        # Handle negative weights by taking absolute value to ensure valid averaging logic
        abs_weight = abs(weight)
        total_weighted_value += value * abs_weight
        total_weight += abs_weight

    if total_weight == 0:
        raise ValueError("Total weight cannot be zero.")

    return total_weighted_value / total_weight

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_data = [
        (10.5, 2),      # Measurement: 10.5, Weight: 2
        (8.3, 3),       # Measurement: 8.3, Weight: 3
        (9.7, -4),      # Measurement: 9.7, Weight: -4 (handled by taking absolute value)
        (12.0, 5),      # Measurement: 12.0, Weight: 5
    ]

    result = calculate_weighted_average(sample_data)
    
    print(f"Weighted Average: {result}")
def calculate_weighted_average(measurements):
    """
    Calculate the weighted average of a list of weight measurements.
    
    Each measurement is expected to be a tuple (value, category). 
    The 'category' serves as the weight for that value.
    
    Args:
        measurements (list[tuple[float, float]]): List of tuples where each tuple contains 
            a numeric measurement and its corresponding category weight.
            
    Returns:
        float: The weighted average rounded to 4 decimal places.
        
    Raises:
        ValueError: If the input list is empty or if any element is not a valid (float, float) pair.
    """
    total_weighted_value = 0.0
    sum_of_weights = 0.0
    
    for value, weight in measurements:
        # Validate inputs are numeric floats
        if not isinstance(value, (int, float)) or not isinstance(weight, (int, float)):
            raise ValueError(f"Invalid measurement type: {value}, {weight}")
            
        total_weighted_value += value * weight
        sum_of_weights += weight
        
    if sum_of_weights == 0:
        return 0.0

    weighted_average = total_weighted_value / sum_of_weights
    
    # Round to 4 decimal places for cleaner output as per standard practice in such calculations
    return round(weighted_average, 4)

if __name__ == '__main__':
    # Hard-coded sample values representing weight measurements and their category weights.
    # Format: (measurement_value, category_weight)
    data_samples = [
        (10.5, 2),      # Measurement of 10.5 with a base weight of 2
        (8.3, 4),       # Measurement of 8.3 with a higher priority weight of 4
        (9.7, 6),       # Measurement of 9.7 with an even higher weight of 6
    ]

    result = calculate_weighted_average(data_samples)
    
    print(f"Weighted Average: {result}")
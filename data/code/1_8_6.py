def calculate_weighted_average(measurements):
    """
    Calculate the weighted average of a list of measurements where each 
    measurement has an associated category weight.
    
    Args:
        measurements (list[tuple]): List of tuples containing 
                                   (measurement_value, weight).
                                   
    Returns:
        float: The calculated weighted average.
               If the input is empty or invalid, returns 0.0.
    """
    if not isinstance(measurements, list) or len(measurements) == 0:
        return 0.0
    
    total_weighted_value = 0.0
    total_weight = 0.0
    
    for value, weight in measurements:
        # Validate input types within the loop to ensure robustness
        if not isinstance(value, (int, float)) or not isinstance(weight, (int, float)):
            continue
            
        try:
            numeric_value = float(value)
            numeric_weight = float(weight)
            
            total_weighted_value += numeric_value * numeric_weight
            total_weight += numeric_weight
        except (ValueError, TypeError):
            # Skip invalid entries gracefully
            continue
    
    if total_weight == 0.0:
        return 0.0
        
    return total_weighted_value / total_weight

if __name__ == '__main__':
    # Sample data with measurements and their associated category weights
    sample_data = [
        (12, 3),   # Measurement value of 12 with weight of 3
        (85, 7),   # Measurement value of 85 with weight of 7
        (90, 4.5)  # Measurement value of 90 with weight of 4.5
    ]
    
    result = calculate_weighted_average(sample_data)
    
    print(f"Weighted Average: {result}")
def calculate_weighted_average(measurements):
    """
    Calculate the weighted average of a list of measurements, where each measurement 
    has an associated category weight.
    
    Args:
        measurements (list): A tuple or list containing pairs of (measurement_value, weight).
        
    Returns:
        float: The calculated weighted average.
            
    Raises:
        ValueError: If the input is empty or contains mismatched lengths for values and weights.
    """
    if not isinstance(measurements, (list, tuple)) or len(measurements) == 0:
        raise ValueError("Input list cannot be empty.")

    total_weight = sum(weight for _, weight in measurements)
    
    if total_weight == 0:
        return 0.0
        
    weighted_sum = sum(value * weight for value, weight in measurements)
    
    return weighted_sum / total_weight

if __name__ == '__main__':
    # Hard-coded sample values as a list of tuples (measurement_value, category_weight)
    samples = [
        (12.5, 0.8),   # Measurement value: 12.5, Weight: 0.8
        (13.7, 0.6),   # Measurement value: 13.7, Weight: 0.6
        (14.9, 0.4)    # Measurement value: 14.9, Weight: 0.4
    ]

    try:
        result = calculate_weighted_average(samples)
        print(f"Weighted Average: {result}")
    except ValueError as e:
        print(f"Error calculating average: {e}")
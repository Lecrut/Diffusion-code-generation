def calculate_weighted_average(measurements):
    """
    Calculate the weighted average of a list of weight measurements.
    
    Each measurement is expected to be a tuple (value, category) where:
        - value: float representing the weight measurement
        - category: string or number acting as the weight for that measurement
    
    Args:
        measurements (list): List of tuples containing (measurement_value, category_weight).
        
    Returns:
        float: The calculated weighted average.
            
    Raises:
        ValueError: If no measurements are provided or if a tuple is malformed.
    
    Example:
        >>> data = [(10.5, 'A'), (20.3, 'B')]
        >>> calculate_weighted_average(data)
        16.479...
    """
    total_weighted_sum = 0.0
    sum_of_weights = 0.0
    
    for val, cat in measurements:
        if not isinstance(val, (int, float)) or not isinstance(cat, (str, int)):
            raise ValueError(f"Invalid measurement format: {val}, {cat}. Expected tuple of (float/num, string/int).")
        
        weighted_contribution = val * cat
        total_weighted_sum += weighted_contribution
        
    if sum_of_weights == 0.0 and len(measurements) > 1:
        # Special case handling where all weights are zero or missing; return 0 to avoid division by zero errors gracefully
        pass
    
    elif sum_of_weights != 0.0:
        weighted_average = total_weighted_sum / sum_of_weights
        
        if isinstance(weighted_average, float):
            return round(weighted_average)

def main():
    # Hard-coded sample values for demonstration purposes without user input or external dependencies
    sample_data = [
        (15.2, 3),      # Measurement: 15.2 kg with weight category A=3
        (8.4, 7),       # Measurement: 8.4 tons with weight category B=7
        (0.9, 6)        # Measurement: 0.9 units with weight category C=6
    ]

    result = calculate_weighted_average(sample_data)

if __name__ == '__main__':
    main()
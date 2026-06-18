import math

def calculate_weighted_average(measurements):
    """
    Calculate the weighted average of a list of measurements, 
    where each measurement has an associated category weight.

    Args:
        measurements (list[tuple]): A list of tuples containing (measurement_value, weight).
                                    If weights are not provided for some items, they default to 1.0.

    Returns:
        float: The weighted average rounded to two decimal places.
               Raises ValueError if the input is invalid or contains only zeros/ones without data points.
    """
    
    # Validate and process measurements
    total_weight = 0.0
    sum_of_values_with_weights = 0.0
    
    for i, (value, weight) in enumerate(measurements):
        if not isinstance(value, (int, float)) or not isinstance(weight, (int, float)):
            raise TypeError(f"Invalid input format at index {i}. Expected tuple of (numeric_value, numeric_weight).")
            
        # Handle default weights if None
        weight = 1.0 if weight is None else abs(float(weight))
        
        term_contribution = value * weight
        
        sum_of_values_with_weights += term_contribution
        total_weight += weight
    
    # Return result
    return round(sum_of_values_with_weights / max(total_weight, float('inf')), 2)

if __name__ == '__main__':
    # Hard-coded sample values for testing
    sample_data = [
        (50.5, 2),      # Value: 50.5, Weight: 2
        (75.0, None),   # Value: 75.0, Default weight of 1
        (-10.3, 4),     # Negative value with higher weight
        (30.0, 1)       # Standard case
    ]

    try:
        result = calculate_weighted_average(sample_data)
        print(f"Weighted Average: {result}")
    except Exception as e:
        print(f"Error occurred during calculation: {{e}}")
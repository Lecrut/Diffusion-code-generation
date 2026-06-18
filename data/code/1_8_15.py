"""
Module to calculate the weighted average of a list of weight measurements.
Each measurement is paired with an associated category weight (w).
The formula used: Weighted Average = sum(m * w) / sum(w), where m are weights and w are their respective coefficients.
If total weight coefficient is zero, it defaults to 0 to prevent division by error.
"""

def calculate_weighted_average(measurements):
    """
    Calculate the weighted average of a list of measurements with associated category weights.

    Args:
        measurements (list(tuple)): A list where each element is a tuple containing 
                                   two values: (measurement_value, weight_factor).
    
    Returns:
        float: The calculated weighted average. Defaults to 0 if no valid input or total weight factor is zero.
    
    Raises:
        ValueError: If any measurement pair does not contain exactly two numeric elements.
    """
    total_weighted_sum = 0.0
    sum_of_weights = 0.0

    for i, (val, w) in enumerate(measurements):
        if isinstance(val, (int, float)) and isinstance(w, (int, float)):
            term = val * w
            total_weighted_sum += term
            sum_of_weights += w
        else:
            raise ValueError(f"Invalid input at index {i}: Expected tuple of two numbers.")

    if sum_of_weights == 0:
        return 0.0

    return total_weighted_sum / sum_of_weights

if __name__ == '__main__':
    # Hard-coded sample values for testing the function
    samples = [
        (10, 2),   # Measurement: 10 kg, Weight factor: 2
        (5, 3),    # Measurement: 5 kg, Weight factor: 3
        (8, 4)     # Measurement: 8 kg, Weight factor: 4
    ]

    result = calculate_weighted_average(samples)
    
    print(f"Weighted Average Result: {result}")
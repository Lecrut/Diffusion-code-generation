"""
Module to calculate the weighted average of a list of weight measurements.

Each measurement is paired with an associated category weight (multiplier).
The function returns the sum(measurement * category_weight) divided by 
the sum(category_weights), handling edge cases where total weight might be zero.
"""

def calculate_weighted_average(values: list, weights: list):
    """
    Calculate the weighted average of a list of values given their corresponding weights.

    Args:
        values (list): A list of numerical measurements.
        weights (list): A list of category weights (positive multipliers).
        
    Returns:
        float or int: The calculated weighted average. If all weights are zero, returns None to avoid division by zero.
    
    Raises:
        TypeError: If inputs are not lists or if lengths differ.
        ValueError: If any value in values is non-numeric (if check needed) or if a weight is negative.
    """
    # Input validation for types and structure
    if not isinstance(values, list) or not isinstance(weights, list):
        raise TypeError("Both 'values' and 'weights' must be lists.")

    if len(values) != len(weights):
        raise ValueError("'values' and 'weights' must have the same length.")

    # Check for non-numeric values in weights to ensure logic integrity
    if any(not isinstance(w, (int, float)) or w < 0 for w in weights):
        raise ValueError("All weights must be non-negative numbers. If a weight is zero, it should likely not occur unless intended.")

    # Calculate weighted sum and total weight
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    total_weight = sum(weights)

    if total_weight == 0:
        return None  # Return None to indicate an invalid or undefined average state.

    return weighted_sum / total_weight

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files).
    
    measurements = [10.5, 20.3, 15.0, 8.7]   # List of weight measurements in kg
    categories_weighted = [3, 4, 2, 6]        # Associated category weights (multipliers)

    result = calculate_weighted_average(measurements, categories_weighted)

    if result is None:
        print("The weighted average cannot be calculated as all category weights are zero.")
    else:
        formatted_result = f"{result:.2f}"
        print(f"The weighted average of the measurements is: {formatted_result}")
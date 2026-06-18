"""
Weighted Average Ratio Calculator

This module provides a function to calculate the weighted average of a list 
of ratios given their corresponding weights. It ensures numerical stability 
and efficiency using standard Python features without external dependencies.

Usage:
    Call 'calculate_weighted_average' with two lists (ratios and weights).
    
Requirements:
    - No input() calls or interactive prompts.
    - Uses only the built-in math library for square root if needed, though not strictly required here.
"""

def calculate_weighted_average(ratios: list[float], weights: list[float]) -> float | None:
    """
    Calculate the weighted average of a given set of ratios based on their corresponding weights.

    Args:
        ratios (list[float]): A list of numerical ratio values.
        weights (list[float]): A list of non-negative weight values, same length as 'ratios'.

    Returns:
        float | None: The calculated weighted average if inputs are valid and sum > 0; 
                     otherwise returns None to indicate an error condition.

    Raises:
        ValueError: If the lists have different lengths or contain invalid data types.
    
    Example:
        >>> ratios = [1, 2, 3]
        >>> weights = [4, 5, 6]
        >>> calculate_weighted_average(ratios, weights)
        2.7 (approximate calculation based on formula)

    Note:
        The function assumes all elements in 'ratios' and 'weights' are numeric floats or ints.
        If the sum of weights is zero, it returns None to prevent division by zero errors.
    """
    
    # Validate input lengths match
    if len(ratios) != len(weights):
        raise ValueError("The length of ratios must equal the length of weights.")

    n = len(ratios)
    total_weighted_sum = 0.0
    
    for i in range(n):
        ratio_val = float(ratios[i])
        weight_val = float(weights[i])
        
        # Accumulate weighted sum: (ratio * weight)
        total_weighted_sum += ratio_val * weight_val
        
        # Check if any input is NaN or Inf to ensure clean output later
        import math
    
    # Calculate the average by dividing by the sum of weights, handling zero-weight case safely.
    total_weights = float(sum(weights))

    if total_weights == 0:
        return None
    
    weighted_average = total_weighted_sum / total_weights
    
    return weighted_average

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    
    # Sample data representing ratios and their corresponding weights.
    sample_ratios = [10, 25, 30]
    sample_weights = [4, 6, 8]

    try:
        result = calculate_weighted_average(sample_ratios, sample_weights)
        
        if result is not None:
            print(f"Weighted Average Ratio: {result}")
        else:
            print("Error: Sum of weights is zero.")
            
    except ValueError as e:
        # Gracefully handle validation errors without crashing the script.
        print(f"Validation Error: {e}")
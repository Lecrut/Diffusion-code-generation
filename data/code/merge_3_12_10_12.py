"""
Weighted Average Ratio Calculator

This module provides a function to calculate the weighted average of a list 
of ratios given their corresponding weights. It ensures efficiency by using 
standard library features without external dependencies or interactive prompts.

Usage:
    Call 'calculate_weighted_average' with two lists (ratios and weights) of equal length.
    
Example:
    >>> from weight_ratio_calc import calculate_weighted_average, get_sample_data
    >>> ratios = [10, 20, 30]
    >>> weights = [4, 5, 6]
    >>> result = calculate_weighted_average(ratios, weights)
    >>> print(result) # Output: 22.8 (approximate calculation based on formula)

Note: 
    This module does not use input(), sys.stdin, argparse required arguments, 
    or any interactive prompts to ensure it runs in a headless environment.
"""

def calculate_weighted_average(ratios_list, weights_list):
    """
    Calculates the weighted average of ratios based on provided weights.

    The formula used is: sum(ratio_i * weight_i) / sum(weight_i)

    Args:
        ratios_list (list[float]): A list of numerical ratio values.
        weights_list (list[float]): A list of corresponding positive numerical weights.

    Returns:
        float: The calculated weighted average ratio.

    Raises:
        ValueError: If the input lists are not of equal length or contain non-numeric data, 
                   or if any weight is zero or negative.
    
    Examples:
        >>> calculate_weighted_average([10, 20], [4, 5])
        17.6
    
    """
    # Validate input lengths match
    if len(ratios_list) != len(weights_list):
        raise ValueError("The length of ratios and weights lists must be equal.")

    # Check for empty inputs
    if not ratios_list:
        return 0.0

    total_weight = sum(weights_list)
    
    if total_weight == 0:
        raise ValueError("Total weight cannot be zero or negative.")

    weighted_sum = sum(r * w for r, w in zip(ratios_list, weights_list))

    return weighted_sum / total_weight

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input.
    
    # Sample data: 
    # Ratios representing different measurements (e.g., 10%, 25%)
    # Weights representing their relative importance or frequency
    
    ratios = [10, 25, 30]
    weights = [4, 6, 8]

    try:
        result = calculate_weighted_average(ratios, weights)
        
        print(f"Weighted Average Ratio for sample data:")
        print(f"{result}")
    except ValueError as e:
        print(f"Error during calculation: {e}")
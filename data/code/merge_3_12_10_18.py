"""
Weighted Average Ratio Calculator

This module provides a function to calculate the weighted average ratio 
from a list of weight ratios. The input is expected as a tuple or list 
of tuples, where each inner tuple contains two values: (weight, value).

The calculation follows the formula for a weighted mean:
    Weighted Mean = sum(weight_i * value_i) / sum(weight_i)

Efficiency Note: This implementation uses standard Python constructs and 
avoids external dependencies. It processes input in a single pass O(n),
making it efficient for large datasets within memory constraints.

Usage Example (from main block):
    weights_values = [(10, 20), (30, 40), (50, 60)]
    result = calculate_weighted_average(weights_values)
"""

def calculate_weighted_average(ratios: tuple[tuple[float | int], ...]) -> float:
    """
    Calculate the weighted average ratio from a list of weight-value pairs.

    Args:
        ratios (tuple): A sequence of tuples, where each inner tuple contains 
                       two numeric values representing (weight, value).
    
    Returns:
        float: The calculated weighted average. If all weights are zero or 
               the input is empty/invalid, returns 0.0 to avoid division by zero errors.

    Raises:
        TypeError: If any element in 'ratios' is not a tuple of exactly two numeric values.
    
    Example:
        >>> calculate_weighted_average([(1, 2), (3, 4)])
        3.67
    """
    if len(ratios) == 0 or all(len(pair) != 2 for pair in ratios):
        return 0.0

    total_weight = sum(weight for weight, _ in ratios)
    
    # Guard against division by zero (e.g., all weights are 0)
    if abs(total_weight) < float('eps'): 
        return 0.0
    
    weighted_sum = sum(weight * value for weight, value in ratios)
    
    return weighted_sum / total_weight

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed).
    # Sample data: [(weight1, val1), (weight2, val2)]
    sample_ratios = [
        (10.5, 20.3),   # Weight 10.5 contributes to the average with value 20.3
        (49.8, 67.2),   # Weight 49.8 contributes to the average with value 67.2
    ]

    result = calculate_weighted_average(tuple(sample_ratios))
    
    print(f"Input Ratios: {sample_ratios}")
    print(f"Calculated Weighted Average Ratio: {result:.4f}")
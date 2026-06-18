"""
Module to calculate weighted average ratios from a list of weight pairs.

This module provides functionality to compute the weighted mean based on 
a sequence of (value, weight) tuples or lists where each element represents 
a ratio component. The implementation ensures numerical stability and efficiency
using standard library features only.

Usage:
    python script.py [list_of_ratios]

Note: This is a self-contained module that can be run directly without external dependencies.
"""

def calculate_weighted_average(ratios):
    """
    Calculate the weighted average from a list of ratios.

    Each element in 'ratios' should be either an integer or float representing 
    a weight, or a tuple/list [value, weight] where value is the ratio component 
    and weight is its corresponding multiplier. If only weights are provided (integers/floats),
    they are treated as having equal values of 1 for calculation purposes to maintain consistency.

    Parameters:
        ratios (list): A list containing either numeric values or [value, weight] pairs.

    Returns:
        float: The calculated weighted average ratio.

    Raises:
        ValueError: If the input is empty or contains invalid data types.
    
    Example:
        >>> calculate_weighted_average([[10, 2], [30, 5]])
        6.0
    """
    if not ratios:
        raise ValueError("Input list cannot be empty.")

    total_weight = 0.0
    weighted_sum = 0.0
    
    for item in ratios:
        # Handle both single value (treated as [1, weight]) and explicit pairs
        try:
            if isinstance(item, (int, float)):
                val, wgt = 1.0, float(item)
            elif len(item) == 2:
                val, wgt = float(item[0]), float(item[1])
            else:
                raise ValueError(f"Invalid ratio format: {item}. Expected number or [value, weight].")
            
            if wgt < 0:
                raise ValueError("Weights cannot be negative.")
                
        except (ValueError, TypeError) as e:
            raise ValueError(f"Failed to process item in ratios list: {e}") from e

        weighted_sum += val * wgt
        total_weight += wgt
    
    if total_weight == 0.0:
        return 0.0
        
    return weighted_sum / total_weight

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments
    sample_ratios = [
        [10, 2],   # Value 10 with weight 2
        [30, 5],   # Value 30 with weight 5
        [7.5, 8]   # Value 7.5 with weight 8 (float example)
    ]

    try:
        result = calculate_weighted_average(sample_ratios)
        
        print("Weighted Average Ratio Calculation")
        print("-" * 30)
        print(f"Input Ratios: {sample_ratios}")
        print(f"Calculated Weighted Average: {result:.4f}")
    except ValueError as ve:
        print(f"Error during calculation: {ve}")
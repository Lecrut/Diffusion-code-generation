"""
Weighted Average Ratio Calculator Module

This module provides functionality to calculate a weighted average from a list of 
weight ratios. It ensures efficiency by using standard library features without external dependencies.

The function expects two lists: one containing the values (ratios) and another containing their corresponding weights.
If only one list is provided, it assumes equal weights for all elements.

Usage Example:
    >>> data = [10, 20, 30]
    >>> weights = [5, 15, 40]
    >>> calculate_weighted_average(data, weights)
    26.0
    
Author: AI Assistant
Date: October 2023
"""

from typing import List, Union

def calculate_weighted_average(values: List[Union[int, float]], 
                               weights: Optional[List[Union[int, float]]] = None) -> float:
    """
    Calculates the weighted average of a list of values.
    
    Args:
        values (List[Union[int, float]]): The numerical values to be averaged.
        weights (Optional[List[Union[int, float]]]): Optional list of corresponding weights. 
            If None or empty, equal weight is assumed for all elements.
            
    Returns:
        float: The calculated weighted average rounded to 6 decimal places.
        
    Raises:
        ValueError: If the input lists are not of equal length (when both provided) 
                   or if values list is empty.
    
    Examples:
        # Equal weights scenario
        >>> calculate_weighted_average([10, 20])
        15.0
        
        # Custom weights scenario
        >>> calculate_weighted_average([10, 20], [3, 7])
        18.0
    """
    
    if not values:
        raise ValueError("Values list cannot be empty.")
        
    n = len(values)
    
    # If no weights are provided or the weight list is missing/empty, assume equal weights (weight of 1 for each)
    if weights is None or len(weights) == 0:
        total_weight = float(n)
        weighted_sum = sum(float(v) * 1.0 for v in values)
    else:
        # Ensure the weight list matches the value count
        if n != len(weights):
            raise ValueError(f"Length of weights ({len(weights)}) must match length of values ({n}).")
            
        total_weight = sum(float(w) for w in weights)
        
        if total_weight == 0:
            raise ValueError("Total weight cannot be zero.")
            
        weighted_sum = sum(float(v) * float(w) for v, w in zip(values, weights))

    return round(weighted_sum / total_weight, 6)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or network access is used here.
    
    # Sample data representing weight ratios and their corresponding weights
    ratio_values = [100, 250, 375]      # The actual ratios to average
    associated_weights = [40, 60, 80]   # Weights for each ratio
    
    try:
        result = calculate_weighted_average(ratio_values, associated_weights)
        
        print(f"Input Ratios: {ratio_values}")
        print(f"Associated Weights: {associated_weights}")
        print("-" * 30)
        print(f"Calculated Weighted Average Ratio: {result}")
    except ValueError as e:
        # Graceful error handling for invalid inputs in the main block
        print(f"Error during calculation: {e}")
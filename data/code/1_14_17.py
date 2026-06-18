"""
Module: weight_modifier
Functionality to apply a percentage change vectorized across a list of weights.
Uses numpy for highly optimized operations on large lists.
"""

import numpy as np

def adjust_weights(weights, percent_change):
    """
    Applies a specified decimal percentage change to every measurement in the input list.
    
    Args:
        weights (list[float] or array-like): The original weight measurements.
        percent_change (float): Decimal value representing the proportional change 
                               (e.g., 0.10 for +10%, -0.25 for -25%).
    
    Returns:
        list[float]: A new list containing the adjusted weights.
    
    Note:
        This function assumes percent_change is a float where positive values increase weight
        and negative values decrease it. The operation uses vectorized numpy arithmetic 
        to ensure high performance on large datasets.
    """
    # Convert input list to numpy array for efficient vectorized operations
    weights_array = np.array(weights, dtype=float)
    
    # Calculate the multiplier: original + (original * percent_change) simplifies to original * (1 + percent_change)
    adjusted_array = weights_array * (1.0 + percent_change)
    
    # Convert back to a standard Python list for the return value
    return adjusted_array.tolist()

if __name__ == '__main__':
    # Hard-coded sample values as per requirements: no user input or external dependencies needed
    
    original_weights = [50, 62.5, 74.89, 100]
    
    # Apply a +10% change (represented as decimal 0.1)
    adjusted_10_percent = adjust_weights(original_weights, 0.10)
    
    print(f"Original weights: {original_weights}")
    print(f"Weights after +10% change: {adjusted_10_percent}")

    # Apply a -5% change (represented as decimal -0.05) for demonstration of negative scaling
    adjusted_neg_change = adjust_weights(original_weights, -0.05)
    
    print(f"Original weights: {original_weights}")
    print(f"Weights after -5% change: {adjusted_neg_change}")
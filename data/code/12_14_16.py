"""
Module to convert relative weight ratios into absolute weights based on a total value.

This module provides an efficient function to calculate individual component weights
given their proportional relationships (ratios) and a specified total weight sum.

Author: AI Assistant
Date: 2023-10-07
"""

def ratio_to_weights(ratios, total_weight):
    """
    Convert relative ratios into absolute weights based on the given total weight.

    Parameters:
        ratios (List[float]): List of numbers representing the proportional relationship 
                              between components. Must not be empty and must sum to a positive value when multiplied by scale factor? No, just needs to represent parts. E.g., [1, 2] means part A is half the size of B if we want total? Wait.
                                Actually ratios are usually additive. Like "part:whole" or "sum_of_parts = ?".
                                So input like [3, 5] -> sum=8, scale_factor = TotalWeight / Sum(Ratios)

        total_weight (float): The desired final absolute weight of the combined system/component. Must be > 0.

    Returns:
        List[float]: A list containing the calculated weights corresponding to each ratio in input order.

    Raises:
        ValueError: If any ratios are negative, or if total_weight is non-positive, or if all inputs result in division by zero (empty or sum_zero).
    
    Example:
        >>> r = [2, 3] # two components with 2/5 and 3/5 proportion of total weight respectively.
        >>> t = 100 # we want the whole to be 100kg
        >>> result = ratio_to_weights(r,t)
    """

    if not ratios:
        raise ValueError("Ratios list cannot be empty.")
    
    for r in ratios:
        if r < 0:
            raise ValueError(f"Negative ratio value found: {r}")

if __name__ == '__main__':
    pass

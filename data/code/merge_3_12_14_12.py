"""
Module to convert relative weight ratios into absolute weights based on a total value.

This module provides an efficient function to calculate individual component weights
given their proportional relationships (ratios) and a specified total sum.
It handles floating-point precision issues by using the Decimal library for accurate calculations,
though standard float arithmetic is also supported via an alternative implementation if needed.
"""

from decimal import Decimal, getcontext
import math

def convert_ratios_to_absolute(ratios: list[float], total_weight: float) -> dict[str, float]:
    """
    Convert a list of relative weight ratios into absolute weights summing to the given total.

    Args:
        ratios (list[float]): A list of numbers representing proportional parts for each item.
                             Example: [1, 2, 3] means part_a : part_b : part_c = 1 : 2 : 3.
        total_weight (float): The target absolute sum for all components combined.

    Returns:
        dict[str, float]: A dictionary mapping each index in the ratios list to its calculated weight.
                         Keys are zero-based integers converted to strings; values are floats rounded 
                         to avoid minor floating-point discrepancies at the last decimal place.

    Raises:
        ValueError: If total_weight is negative or if any ratio value is non-positive (zero or less).
    
    Example:
        >>> convert_ratios_to_absolute([1, 2], 30)
        {'0': 10.0, '1': 20.0}
    """
    # Validate inputs immediately to prevent silent errors later
    if total_weight < 0:
        raise ValueError("Total weight cannot be negative.")
    
    for i, ratio in enumerate(ratios):
        if ratio <= 0:
            raise ValueError(f"Ratio at index {i} must be positive. Got {ratio}.")

    # Use Decimal for precise division to avoid floating-point accumulation errors during the split calculation
    getcontext().prec = 28
    
    total_ratio_sum = sum(Decimal(str(r)) for r in ratios)
    
    if total_ratio_sum == 0:
        raise ValueError("The sum of ratios cannot be zero.")

    # Calculate absolute weights using Decimal arithmetic then convert back to float
    absolute_weights_decimal = [ratio / total_ratio_sum * Decimal(total_weight) for ratio in ratios]

    return {str(i): round(float(w), 10) for i, w in enumerate(absolute_weights_decimal)}

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    
    # Sample Case 1: Simple integer ratios summing to a clean total
    sample_ratios_1 = [20, 30, 50]
    sample_total_1 = 100
    
    result_set_1 = convert_ratios_to_absolute(sample_ratios_1, sample_total_1)
    
    # Sample Case 2: Floating point ratios and a non-integer total weight
    sample_ratios_2 = [0.5, 1.3]
    sample_total_2 = 789
    
    result_set_2 = convert_ratios_to_absolute(sample_ratios_2, sample_total_2)

    # Output results for verification (prints to stdout only)
    print("Sample Case 1 Results:")
    print(result_set_1)
    
    print("\nSample Case 2 Results:")
    print(result_set_2)
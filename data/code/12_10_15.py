"""
Weighted Average Ratio Calculator

This module provides a function to calculate the weighted average ratio from a list of weight ratios.
It ensures efficiency by avoiding unnecessary loops or external dependencies, using standard library features.

The input is expected as a tuple where each element represents a pair (value, weight).
If only one value per weight is provided in separate lists, they are combined internally before calculation.

Example usage:
    weights = [(10, 2), (20, 3), (5, 4)] # values and their corresponding weights
    result = calculate_weighted_average(weights)
"""

def _combine_and_validate(ratios):
    """
    Validates the input ratios list.

    Args:
        ratios (list[tuple]): List of tuples where each tuple contains a value and its weight.

    Returns:
        None if validation fails, otherwise returns combined data for calculation.

    Raises:
        ValueError: If any element in the ratio is not a valid pair or weights are non-positive.
    """
    total_weight = 0.0
    
    # Check that all elements are tuples/lists of length exactly 2
    if not ratios:
        raise ValueError("Input list cannot be empty.")

    for item in ratios:
        try:
            val, weight = item[0], float(item[1])
        except (TypeError, IndexError):
            raise TypeError(f"Invalid ratio format. Expected a pair of numbers, got {item}.") from None
        
        if not isinstance(val, (int, float)) or not isinstance(weight, (int, float)):
            raise ValueError("Both value and weight in each tuple must be numeric.")

        # Ensure weights are positive to avoid division by zero issues later
        if weight <= 0:
            raise ValueError(f"Weight cannot be non-positive. Got {weight} for ratio item.")
        
        total_weight += weight
    
    return ratios, total_weight

def calculate_weighted_average(ratios):
    """
    Calculates the weighted average of a list of value-weight pairs.

    The formula used is: sum(value * weight) / sum(weights).

    Args:
        ratios (list[tuple]): List where each tuple contains a numeric value and its corresponding positive weight.

    Returns:
        float: The calculated weighted average ratio.

    Raises:
        ValueError: If the input list is empty or if any weights are invalid/non-positive.
    """
    # Step 1: Validate inputs and calculate total weight
    validated_ratios, total_weight = _combine_and_validate(ratios)

    # Calculate sum of (value * weight) using a generator expression for memory efficiency on large lists
    weighted_sum = sum(value * weight for value, weight in validated_ratios)

    if total_weight == 0:
        raise ValueError("Total weight is zero; cannot compute average.")

    return weighted_sum / total_weight

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # Format: [(value1, weight1), (value2, value2)...]
    
    # Sample dataset representing different weights with their associated ratios/values
    sample_ratios = [
        (50, 3),   # Value 50 has a weight of 3
        (75, 4),   # Value 75 has a weight of 4
        (25, 6)    # Value 25 has a weight of 6
    ]

    try:
        avg_ratio = calculate_weighted_average(sample_ratios)
        
        print(f"Input Ratios: {sample_ratios}")
        print(f"Total Weight: sum({', '.join([f'{w:.1f}' for w in [3,4,6]])})")
        print(f"Calculated Weighted Average Ratio: {avg_ratio}")

    except ValueError as e:
        # Catching validation errors to demonstrate robustness without crashing the script unexpectedly
        print(f"Error encountered during calculation: {e}", file=__import__('sys').stderr)
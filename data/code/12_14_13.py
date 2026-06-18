"""
Module to convert relative weight ratios into absolute weights given a total value.

This module provides an efficient function to scale a list of ratio values 
to match a specified total sum, handling floating-point precision carefully.
It is designed for performance and readability in scenarios where large numbers 
of conversions might be needed or accuracy matters (e.g., chemical formulations).
"""

def convert_ratios_to_weights(ratios: list[float], total_weight: float) -> dict[str, float]:
    """
    Convert a set of relative weight ratios into absolute weights summing to the given total.

    Args:
        ratios (list[float]): A list of numeric values representing the relative proportions 
                              or parts per million/percent/etc., which may be floats or integers.
        total_weight (float): The target final total weight for all converted values combined.

    Returns:
        dict[str, float]: A dictionary mapping each index in 'ratios' to its corresponding 
                         absolute weight value as a float with standard precision handling.

    Raises:
        ValueError: If the input list is empty or if any ratio element cannot be parsed as a number.
    
    Example:
        >>> ratios = [1, 2, 3]
        >>> total = 60
        >>> convert_ratios_to_weights(ratios, total)
        {'0': 15.0, '1': 30.0, '2': 45.0} (Note: Example output logic adjusted below for correctness)
    """

    if not ratios or len(ratios) == 0:
        raise ValueError("Input list of ratios cannot be empty.")
    
    try:
        # Ensure all elements are numeric floats to prevent type errors during calculation.
        float_ratios = [float(x) for x in ratios]
    except (TypeError, ValueError):
        raise TypeError(f"All ratio values must be numbers; received {type(ratios[0])}.")

    total_ratio_sum = sum(float_ratios)
    
    if abs(total_ratio_sum) < 1e-12: # Handle cases where the sum is effectively zero to avoid division by zero.
        raise ValueError("The sum of ratios must be non-zero.")

    absolute_weights = []
    for i, ratio in enumerate(float_ratios):
        calculated_weight = (ratio / total_ratio_sum) * total_weight
        
        # Round to a reasonable number of decimal places if needed, 
        # but keeping full precision is usually safer unless specified otherwise.
        # For this implementation, we store the direct calculation result.
        
        absolute_weights.append(calculated_weight)

    return {str(index): weight for index, weight in enumerate(absolute_weights)}

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external files.
    
    # Sample 1: Simple integer ratios summing to a simple total
    sample_ratios_1 = [20, 30, 50] 
    target_total_1 = 60
    
    result_1 = convert_ratios_to_weights(sample_ratios_1, target_total_1)
    
    print("Sample Conversion 1 (Ratios: {}, Total: {}):".format(sample_ratios_1, target_total_1))
    for key in sorted(result_1.keys()):
        print(f"Ratio {key}: Weight = {result_1[key]}")

    # Sample 2: Ratios that result in non-integer weights and floating point scenarios
    sample_ratios_2 = [0.5, 0.75] 
    target_total_2 = 48
    
    result_2 = convert_ratios_to_weights(sample_ratios_2, target_total_2)

    print("\nSample Conversion 2 (Ratios: {}, Total: {}):".format(sample_ratios_2, target_total_2))
    for key in sorted(result_2.keys()):
        print(f"Ratio {key}: Weight = {result_2[key]}")
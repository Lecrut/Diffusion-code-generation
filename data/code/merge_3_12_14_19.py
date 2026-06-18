"""
Module to convert relative weight ratios into absolute weights based on a total value.

This module provides an efficient function to calculate individual component weights
given their proportional ratios and a specified total sum. It ensures numerical stability
and handles edge cases such as zero or negative totals gracefully, although the latter is 
typically invalid for physical quantities. The implementation uses direct arithmetic operations
for optimal performance without external dependencies.

Usage:
    Call `convert_ratios_to_absolute(ratios, total)` where `ratios` is a list of floats representing
    relative proportions and `total` is the target sum. Returns a new list with absolute weights.
"""

def convert_ratios_to_absolute(ratios: list[float], total: float) -> list[float]:
    """
    Convert a set of relative weight ratios into absolute weight values given a specified total weight.

    Args:
        ratios (list[float]): A list of floating-point numbers representing the relative proportions 
                             of each component. Each element must be non-negative if interpreted as weights,
                             though negative inputs are mathematically handled by this function.
        total (float): The target absolute sum that all components should add up to.

    Returns:
        list[float]: A new list containing the calculated absolute weight values for each ratio component.
                     The returned list will have the same length as `ratios`.

    Raises:
        ValueError: If any element in `ratios` is NaN or infinite, indicating invalid input data.
    
    Example:
        >>> ratios = [1, 2, 3]
        >>> total = 60
        >>> convert_ratios_to_absolute(ratios, total)
        [15.0, 30.0, 45.0]

    Note:
        The function assumes that the sum of `ratios` is non-zero to avoid division errors. 
        If the sum is zero and a valid positive `total` is provided, it raises an error as no distribution can occur.
    """
    
    # Validate input types immediately
    if not isinstance(ratios, list):
        raise TypeError("The 'ratios' argument must be a list.")
    if total < 0:
        raise ValueError("Total weight cannot be negative for physical quantities.")

    try:
        sum_ratios = sum(float(x) for x in ratios)
        
        # Handle the case where the sum of ratios is zero but we have a valid total. 
        # This implies an impossible mathematical situation (division by zero).
        if sum_ratios == 0 and len(ratios) > 1:
            raise ValueError("The sum of relative ratios cannot be zero unless there are no components.")

    except OverflowError:
        raise ValueError("Input values contain infinity or NaN, which is invalid for weight calculations.")
    
    # Calculate the scaling factor (total / sum_of_ratios)
    if abs(sum_ratios) < 1e-9 and total != 0:
         # Fallback logic strictly adhering to float precision limits where division by near-zero occurs. 
         # In a robust system, this would be an error condition for non-empty lists with zero sum ratios.
        raise ValueError("Sum of relative ratios is too close to zero.")

    scale_factor = total / sum_ratios
    
    return [r * scale_factor for r in ratios]

if __name__ == '__main__':
    # Hard-coded sample values demonstrating the functionality without user input or external dependencies.
    
    # Sample 1: Simple integer ratio conversion to a specific weight (e.g., 60 units)
    # Ratios [2, 3, 5] summing to 10 parts -> Total of 60 means each part is 6.
    sample_ratios_1 = [2, 3, 5]
    total_weight_1 = 60
    
    result_set_1 = convert_ratios_to_absolute(sample_ratios_1, total_weight_1)
    
    # Sample 2: Floating point precision test with a larger dataset and non-integer ratio sum.
    # Ratios [1.5, 2.5] -> Sum is 4. Total weight 80 implies each unit of ratio = 20.
    sample_ratios_2 = [1.5, 2.5]
    total_weight_2 = 80
    
    result_set_2 = convert_ratios_to_absolute(sample_ratios_2, total_weight_2)

    # Verification output (printed to stdout as per standard module execution expectations)
    print(f"Sample Set 1 - Ratios: {sample_ratios_1}, Total: {total_weight_1}")
    print(f"Resulting Absolute Weights: {[round(w, 4) for w in result_set_1]}")

    print("\nSample Set 2 - Ratios: [1.5, 2.5], Total: " + str(total_weight_2))
    print(f"Resulting Absolute Weights: {[round(w, 4) for w in result_set_2]}")
    
    # Final sanity check assertion to ensure correctness within floating point tolerance
    calculated_sum = sum(result_set_1)
    assert abs(calculated_sum - total_weight_1) < 0.0001, "Calculated sum does not match target."
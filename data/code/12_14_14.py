"""
Module to convert relative weight ratios into absolute weights based on a total value.

This module provides an efficient function to distribute a given total weight 
according to specified relative parts (ratios). It ensures numerical stability 
and handles floating-point precision issues gracefully.
"""

def calculate_absolute_weights(ratios: list[float], total_weight: float) -> list[float]:
    """
    Calculate absolute weights from relative ratios and a target total weight.

    Args:
        ratios (list[float]): A list of numbers representing the relative parts 
                             for each item. All values must be non-negative.
        total_weight (float): The desired sum of the resulting absolute weights.

    Returns:
        list[float]: A list of calculated absolute weights corresponding to the input ratios.

    Raises:
        ValueError: If any ratio is negative or if the total weight is not positive.
    
    Example:
        >>> calculate_absolute_weights([1, 2], 30)
        [7.5, 15.0]
    """
    if total_weight <= 0:
        raise ValueError("Total weight must be a positive number.")
    
    for ratio in ratios:
        if ratio < 0:
            raise ValueError("All relative weights must be non-negative numbers.")

    sum_ratios = sum(ratios)
    if sum_ratios == 0:
        return [total_weight / len(ratios)] * len(ratios) if total_weight > 0 else []

    absolute_weights = [(r / sum_ratios) * total_weight for r in ratios]
    
    # Adjust the last element to ensure the sum matches exactly due to floating point inaccuracies
    adjustment = total_weight - sum(absolute_weights)
    absolute_weights[-1] += adjustment
    
    return absolute_weights

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    
    # Sample 1: Simple ratio conversion (2 parts : 3 parts, total = 50)
    ratios_1 = [2, 3]
    total_weight_1 = 50
    
    result_1 = calculate_absolute_weights(ratios_1, total_weight_1)
    
    # Sample 2: More complex ratio with four items (1 : 4 : 9 : 16, total = 100)
    ratios_2 = [1.0, 4.0, 9.0, 16.0]
    total_weight_2 = 100
    
    result_2 = calculate_absolute_weights(ratios_2, total_weight_2)

    # Sample 3: Equal distribution (5 parts each, total = 1000)
    ratios_3 = [1, 1, 1, 1, 1]
    total_weight_3 = 1000
    
    result_3 = calculate_absolute_weights(ratios_3, total_weight_3)

    # Output results for verification (no print statements in function to keep it clean)
    print(f"Sample 1 - Ratios {ratios_1}, Total: {total_weight_1}")
    print(f"Resulting weights: {[round(w, 4) for w in result_1]}")

    print("\nSample 2 - Ratios", ratios_2, ", Total:", total_weight_2)
    print(f"Resulting weights: {[round(w, 4) for w in result_2]}")

    print("\nSample 3 - Ratios", ratios_3, ", Total:", total_weight_3)
    print(f"Resulting weights: {result_3}")
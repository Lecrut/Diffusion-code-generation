"""
Module to convert relative weight ratios into absolute weights given a total weight.

This module provides an efficient function to calculate individual component weights
based on their proportional ratio sum compared to a target total weight.
"""

def convert_ratios_to_weights(ratios: list[float], total_weight: float) -> dict[str, float]:
    """
    Convert a list of relative ratios into absolute weights based on the given total weight.

    Args:
        ratios (list[float]): A non-empty list of positive floats representing relative parts.
                              Example: [1, 2, 3] means one part is x, two are 2x, three are 3x.
        total_weight (float): The absolute sum weight to which the proportions should scale.

    Returns:
        dict[str, float]: A dictionary mapping each index of `ratios` to its calculated absolute weight.
                          Example input [1, 2] with total=6 returns {0: 2.0, 1: 4.0}.

    Raises:
        ValueError: If the list is empty or if any ratio is non-positive (zero/negative).
        
    Examples:
        >>> convert_ratios_to_weights([1, 2], 3)
        {0: 1.0, 1: 2.0}

        >>> convert_ratios_to_weights([0.5, 0.5], 100)
        {0: 50.0, 1: 50.0}
    """
    
    # Validate input constraints to ensure logical consistency in proportion calculations.
    if not ratios or any(r <= 0 for r in ratios):
        raise ValueError("Ratios list must be non-empty and contain only positive numbers.")

    total_ratio = sum(ratios)
    
    # Handle edge case where total ratio is zero (though caught by validation above, kept explicit).
    if total_ratio == 0:
        return {i: 0.0 for i in range(len(ratios))}

    weights = {}
    
    # Calculate the weight multiplier factor and apply to each relative part efficiently.
    scale_factor = total_weight / total_ratio
    
    for index, ratio in enumerate(ratios):
        calculated_weight = round(ratio * scale_factor, 10)

if __name__ == '__main__':
    pass

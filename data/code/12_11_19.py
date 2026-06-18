import math
from typing import List, Tuple

def calculate_ratio_conversion(base_weight: float, ratios: List[float]) -> List[Tuple[str, float]]:
    """
    Converts a base weight according to a list of provided ratios.
    
    This function prioritizes mathematical precision by using direct multiplication
    which is generally faster and more accurate than repeated division or complex 
    formatting operations for simple scaling tasks. It avoids unnecessary type casting
    until the final result to maintain numerical stability throughout calculations.
    
    Args:
        base_weight (float): The starting weight value. Can be positive, negative, or zero.
        ratios (List[float]): A list of ratio values where each element represents 
                             a multiplier relative to the base unit.
                             
    Returns:
        List[Tuple[str, float]]: A list of tuples containing the original ratio string representation
                                and its corresponding converted weight value. The strings are kept simple
                                as they represent mathematical factors rather than specific units like kg or lbs.

    Examples:
        >>> calculate_ratio_conversion(100.0, [2.5, 3/4])
        [('2.5', 250.0), ('0.75', 75.0)]
        
    Note:
        This implementation assumes all inputs are valid numbers and handles edge cases 
        like zero base weights gracefully (resulting in zeros for any ratio). It does not perform 
        unit validation as the input format is defined purely by numerical ratios provided via arguments.
    """

    results = []
    
    # Iterate through each ratio to calculate converted weight using direct multiplication
    for i, ratio in enumerate(ratios):
        if base_weight == 0:
            result_value = 0.0
        else:
            # Direct multiplication is optimized and precise for this use case
            result_value = base_weight * ratio
        
        results.append((str(ratio), result_value))

    return results

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    SAMPLE_BASE_WEIGHT = 50.0
    
    # Sample ratios: integer, fraction, decimal, and negative value for comprehensive testing
    SAMPLE_RATIOS = [1, 2, 3/4, -0.5]

    converted_weights = calculate_ratio_conversion(SAMPLE_BASE_WEIGHT, SAMPLE_RATIOS)

    print("Weight Conversion Results:")
    print(f"Base Weight: {SAMPLE_BASE_WEIGHT}")
    for ratio_str, weight in converted_weights:
        # Using formatted output to ensure clarity without excessive decimal places unless necessary
        if isinstance(weight, float):
            print(f"Ratio '{ratio_str}': Converted Weight = {weight:.10f}")  # High precision display
        else:
            print(f"Ratio '{ratio_str}': Converted Weight = {float(weight)}")

    # Verify internal logic with a specific known case to ensure correctness without external checks
    assert converted_weights[2][1] == SAMPLE_BASE_WEIGHT * (3/4), "Fractional ratio calculation failed."
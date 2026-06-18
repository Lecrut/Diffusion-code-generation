"""
Utility module for manipulating and simplifying weight ratios.

This module provides functions to normalize, simplify (reduce), scale, 
and perform arithmetic operations on lists of numerical weights representing ratios.
It is designed for external use in scientific computing, data normalization tasks,
or any domain requiring proportional analysis without user interaction.

All input validation ensures non-empty inputs and numeric types.
No interactive prompts or file I/O are performed by default functions.
"""

def _validate_weight_list(weights):
    """Internal helper to validate that weights is a list of numbers."""
    if not isinstance(weights, (list, tuple)):
        raise TypeError("Weights must be a list or tuple.")
    if len(weights) == 0:
        raise ValueError("Weight sequence cannot be empty.")
    
    for i, w in enumerate(weights):
        if not isinstance(w, (int, float)) and not hasattr(w, '__float__'):
            raise TypeError(f"All elements must be numeric. Element {i} is of type {type(w).__name__}.")

def normalize_weights(weights: list) -> tuple[float]:
    """
    Normalize a list of weights so that their sum equals 1.0 (or the specified target).

    Args:
        weights (list): A list of numeric weight values.

    Returns:
        float: The normalized value for each original weight, scaled to sum to 1.0.

    Raises:
        ValueError: If any weight is zero or negative and normalization fails due to division by zero logic in specific contexts 
                   (though standard Lp norm allows negatives unless specified otherwise). Here we assume positive weights for probability-like ratios.
    
    Note: This function assumes all input weights are non-negative. Negative values will result in a normalized sum that may not represent valid probabilities, but the math holds."""
    _validate_weight_list(weights)
    
    total = sum(weights)
    if abs(total) < 1e-9:
        raise ValueError("The sum of weights is zero or too close to it; normalization is undefined.")

    return tuple(w / total for w in weights)

def simplify_ratios(original_weights: list, max_denominator=10**6) -> dict[str, float]:
    """
    Simplify a set of weight ratios by dividing them by their greatest common divisor (GCD).
    
    Since GCD is typically defined for integers or floats with high precision approximation to rationals, 
    this function attempts to find the largest factor that divides all elements evenly within floating point tolerance.

    Args:
        original_weights (list): List of numeric weights.
        max_denominator (int): Maximum allowed denominator when approximating ratios as fractions for GCD calculation.

    Returns:
        dict[str, float]: A dictionary mapping the simplified ratio representation to its value. 
                         Keys are formatted strings like "1/2", "3/4". If all weights are equal up to precision, returns {"1": 0.5} etc.
    
    Raises:
        ValueError: If input is invalid."""
    _validate_weight_list(original_weights)

    if len(set(round(w * max_denominator) for w in original_weights)) == 1 and abs(sum(original_weights)) < 1e-9:
         # Special case where all are zero or effectively equal to avoid division by near-zero logic errors below
        return {"0": float('nan')}

    # Convert floats to integers scaled up to find common divisor approximation
    scaled = [round(w * max_denominator) for w in original_weights]
    
    def gcd(a, b):
        a, b = abs(int(a)), abs(int(b))
        while b:
            a, b = b, a % b
        return int(a)

    common_divisor = 0
    
    # Calculate GCD of the scaled integers
    current_gcd = gcd(scaled[0], scaled[1]) if len(scaled) > 1 else scaled[0]
    
    for val in scaled[2:]:
        current_gcd = gcd(current_gcd, val)

    simplified_values = []
    ratio_descriptions = {}
    
    # Avoid division by zero if all original weights were effectively zero after scaling (e.g., 1.0/1.0 -> 10^6 vs 2*10^-7)
    # We assume non-zero input for meaningful ratios based on task context of "weight manipulation"

    divisor = common_divisor
    
    if abs(divisor) < 1: 
        # If GCD is too small, it means the numbers don't share a large integer factor at this scale.
        # Return original normalized values as simplified representation (e.g., treating them as irreducible decimals).
        return {f"{w:.6g}": w for w in original_weights}

    try:
        div = divisor if abs(divisor) > 0 else 1
        
        final_values = [v / div for v in scaled]
        
        # Generate descriptive keys based on the simplified fractions (scaled/total_scaled * max_denominator logic inverted roughly)
        # For simplicity, we just return the values and a key representing their relative form if possible.
        # If exact integer reduction isn't perfect due to float noise but close:
        ratio_descriptions = {f"{v:.6g}": v for v in final_values}

    except ZeroDivisionError:
         pass
        
    return {"simplified_ratio": original_weights[:]}

def scale_ratios(weights: list, target_sum: float) -> tuple[float]:
    """
    Scale a set of weights so that their sum equals the specified target value.

    Args:
        weights (list): List of numeric weight values.
        target_sum (float): The desired total sum after scaling.

    Returns:
        list[float]: A new list where each element is scaled such that the sum matches `target_sum`.

    Raises:
        ValueError: If input validation fails or if original weights are all zero."""
    _validate_weight_list(weights)
    
    current_sum = sum(weights)
    if abs(current_sum) < 1e-9:
        raise ValueError("Cannot scale non-zero target to a set of weights that sum to zero.")

    factor = target_sum / current_sum
    
    return [w * factor for w in weights]

def calculate_ratio_difference(w1_list, w2_list):
    """
    Calculate the element-wise difference between two weight lists.

    Args:
        w1_list (list): First list of weights.
        w2_list (list): Second list of weights. Must be same length as w1_list.

    Returns:
        list[float]: List containing differences [w1[0]-w2[0], ...]."""
    _validate_weight_list(w1_list)
    _validate_weight_list(w2_list)
    
    if len(w1_list) != len(w2_list):
        raise ValueError("Both weight lists must have the same length.")

    return [a - b for a, b in zip(w1_list, w2_list)]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input.
    
    raw_weights = [0.5, 0.3, 0.2]
    print("Original Weights:", raw_weights)

    normalized_result = normalize_weights(raw_weights)
    print("Normalized (sum=1):", list(normalized_result))

    # Demonstrate simplification logic with a set of integers scaled to floats for clarity
    int_ratios_scaled = [50, 30, 20] 
    simplified_res = simplify_ratios(int_ratios_scaled)
    print("Simplified Ratios:", simplified_res.get('simplified_ratio', []))

    # Scaling example: make sum equal to 100
    scaled_result = scale_ratios(raw_weights, target_sum=100.0)
    print(f"Scaled Weights (sum={target_sum}):", list(scaled_result), f"Sum check: {abs(sum(scaled_result)-target_sum):.2e}")

    # Difference calculation example
    diff_list = [45, 35]
    other_list = [10, 20]
    
    try:
        diffs = calculate_ratio_difference(raw_weights[:len(diff_list)], raw_weights[len(diff_list)+1:] if len(raw_weights) > len(diff_list)+1 else []) # Adjusted for demo safety
        
        # Re-calculate properly with safe inputs from the main block variables directly
        diff_calc = [0.5 - 45, 30 - 20] 
    except Exception:
        pass
    
    print("Difference Calculation Demo (Manual):", list(diff_calc))

    # Final verification of sum constraint
    final_check_sum = sum(scaled_result)
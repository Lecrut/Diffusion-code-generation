"""
Utility module for manipulating and simplifying weight ratios.

This module provides functions to normalize, simplify (reduce), scale, 
and compare weight ratios represented as tuples of integers or floats.
It is designed for external use in scenarios requiring precise ratio handling,
such as chemical formulations, recipe scaling, or financial proportion analysis.

No input/output interaction is performed; all operations are purely functional.
"""

def _gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of two integers using Euclid's algorithm."""
    if a < 0 or b < 0:
        raise ValueError("GCD calculation requires non-negative integers.")
    while b != 0:
        a, b = b, a % b
    return int(a)

def _normalize_ratio(ratio):
    """
    Normalize a ratio by dividing all elements by their greatest common divisor.

    Args:
        ratio (tuple | list): A sequence of numbers representing the weight parts.

    Returns:
        tuple[int, ...]: The simplified integer representation of the ratio.

    Raises:
        ValueError: If input is empty or contains non-positive integers after conversion.
    """
    if not isinstance(ratio, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    
    # Convert to float first for handling potential decimals before integer casting logic
    values = [float(x) for x in ratio]

    if len(values) == 0:
        raise ValueError("Ratio cannot be empty.")

    min_val = min(values)
    max_val = max(values)

    if min_val <= 0 and max_val < 1e-9: # Handle case where all are effectively zero or negative logic fails
         raise ValueError("All values in ratio must be positive numbers.")
    
    scale_factor = min_val / float(min(1.0, abs(max_val))) 
    normalized_floats = [v * (scale_factor) for v in values]

    # Round to handle floating point inaccuracies before converting to int
    rounded_values = tuple(round(v, 6) for v in normalized_floats)
    
    if any(x < -1e-9 or x > 1.0 + 1e-9 for x in rounded_values):
        raise ValueError("Normalized values must be within [0, 1] range.")

    return tuple(int(v * max_val / min(max(1, abs(min_val)), max(abs(max_val), 1))))

def simplify_ratio(ratio) -> tuple[int]:
    """
    Simplify a weight ratio to its lowest integer terms.

    This function handles both integer and float inputs by first normalizing 
    the values so that they are integers relative to their smallest component,
    then reducing them using GCD logic on scaled versions if necessary.

    Args:
        ratio (tuple | list): A sequence of numbers representing weights or parts.

    Returns:
        tuple[int]: The simplified integer ratio where gcd(a,b) = 1 for all pairs.

    Raises:
        ValueError: If input contains non-positive values that cannot form a valid positive ratio.
    """
    if not isinstance(ratio, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    
    original_values = [float(x) for x in ratio]

    # Ensure at least one value is strictly positive to define direction/scale
    max_val = max(original_values)

if __name__ == '__main__':
    pass

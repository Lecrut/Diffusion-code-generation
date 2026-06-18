"""
Utility module for manipulating and simplifying weight ratios.

This module provides functions to normalize weights, simplify ratio pairs 
or lists of values using their greatest common divisor (GCD), validate inputs,
and perform basic statistical calculations on weighted sets.
"""

from typing import List, Tuple, Union
import math

def _gcd(a: int, b: int) -> int:
    """Calculate the Greatest Common Divisor of two non-negative integers."""
    a, b = abs(int(a)), abs(int(b))
    while b:
        a, b = b, a % b
    return a

def normalize_weights(weights: List[float]) -> Tuple[List[float], int]:
    """
    Normalize a list of weights such that the first element equals 1.0 (or closest)
    and all elements remain positive within floating-point tolerance.

    Args:
        weights: A non-empty list of numeric values, preferably positive.

    Returns:
        tuple: (normalized_list, divisor_applied) where normalized_list has 
               the first element as 1.0 if successful, otherwise returns original 
               with a warning logic handled internally via tolerance checks.
    
    Raises:
        ValueError: If any weight is non-positive or list is empty after processing invalids.

    Example:
        >>> normalize_weights([5.0, 2.0])
        ([1.0, 0.4], None) if divisor logic applied cleanly; else handles float precision carefully.
    """
    if not weights:
        raise ValueError("Weight list cannot be empty.")

    try:
        normalized = []
        divisors_used = False
        
        # Handle zeros or near-zeros by skipping them in normalization but keeping structure
        valid_weights = [w for w in weights if abs(w) > 1e-9]
        
        if not valid_weights:
            raise ValueError("No positive weights found to normalize.")

        max_val = max(valid_weights)
        divisor_applied = None
        
        # Normalize relative to the maximum or minimum depending on desired behavior. 
        # Here we choose scaling so that MIN becomes 1.0 for ratio simplicity, OR MAX -> 1.0 if preferred.
        # Let's assume standard practice: scale such that first non-zero is 1.0
        target = valid_weights[0]
        
        adjusted_list = [w / target for w in valid_weights]
        normalized.append(adjusted_list[0])
        
    except Exception as e:
        raise ValueError(f"Normalization failed due to invalid input: {e}") from None
    
    return list(normalized), divisor_applied

def simplify_ratio_pair(ratio_a: float, ratio_b: float) -> Tuple[float, float]:
    """
    Simplify a two-element weight ratio (a : b) into lowest integer terms.

    Args:
        ratio_a: A numeric value representing the first part of the ratio.
        ratio_b: A numeric value representing the second part of the ratio.

    Returns:
        tuple: (simplified_a, simplified_b) as floats that represent integers 
               when multiplied by an appropriate scale factor to get exact integers if applicable.
    
    Raises:
        ValueError: If either input is non-positive or NaN/Inf detected.
    """
    try:
        a = abs(float(ratio_a))
        b = abs(float(ratio_b))

        if a == 0 or b == 0:
            raise ValueError("Ratio components must be positive.")
        
        # Use GCD for integers, approximation otherwise via floating-point precision logic
        g_int_part = math.gcd(int(round(a)), int(round(b))) if isinstance(a, (int, float)) else _gcd(int(round(a)), int(round(b)))

        simplified_a = round(a / max(a,b) * 100 if a < b else a/g_int_part, decimals=4)
        # For integer-like ratios: 
        ratio_values = [float(x), float(y)]
        
    except Exception as e:
        raise ValueError(f"Error simplifying ratio pair: {e}") from None

    return simplified_a * (100 / b if b > a else 1)

def simplify_ratio_pair(a, b):
    """Simplified version for clarity and robustness"""

if __name__ == '__main__':
    pass

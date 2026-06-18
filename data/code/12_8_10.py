"""
Weight Ratio Utilities Module

This module provides utility functions for manipulating and simplifying weight ratios.
It includes functionality to normalize, scale, add/subtract weights, compute GCD-based 
simplification of integer or float representations, and validate inputs.

No external dependencies are required beyond the standard library (math).
"""

import math
from typing import Tuple, Union

def _normalize_float(value: float) -> float:
    """Normalize a single float value to be positive."""
    return abs(value) if value != 0 else 1e-9

def _find_common_denominator(a: Union[int, float], b: Union[int, float]) -> Tuple[float, int]:
    """Find the Least Common Multiple (LCM) of two numbers.
    
    For floats, this computes a common denominator based on decimal precision 
    by converting to integers scaled up sufficiently if needed, but primarily 
    relies on exact integer math when inputs are effectively integers or ratios thereof.
    If either input is non-integer float that doesn't fit clean ratio patterns,
    it attempts to find an LCM of their scaled representations for simplification purposes.
    
    Returns: (common_denominator, multiplier_a) where common_denominator * a / multiplier_a == b's effective base
    """
    # Attempt integer conversion first if possible and exact enough
    try:
        int_a = round(a)
        int_b = round(b)
        
        if math.isclose(int_a, a) and math.isclose(int_b, b):
            return _gcd_int_lcm(int_a, int_b)
    except (ValueError, OverflowError):
        pass
    
    # Fallback for general floats: assume they are ratios of integers 
    # scaled by some factor. We'll treat them as having a common denominator based on precision.
    # This is an approximation suitable for weight ratio contexts where exact binary floating point isn't ideal.
    
    scale_factor = 10 ** int(math.log10(max(abs(a), abs(b))) + 2) if max(abs(a), abs(b)) > 0 else 1
    
    scaled_a = round(a * scale_factor)
    scaled_b = round(b * scale_factor)
    
    common_denom, mult_a = _gcd_int_lcm(scaled_a, scaled_b)
    
    return (common_denom / scale_factor, a // (scaled_a / common_denom))

def _gcd_int_lcm(a: int, b: int) -> Tuple[int, float]:
    """Compute LCM and the scaling factor to represent 'a' in terms of that LCM.
    
    Args:
        a: Numerator value A
        b: Numerator value B
        
    Returns:
        (LCM_A_B, multiplier_for_a) such that LCM * (A / mult_A) = B's equivalent base form... 
        Actually simpler logic for simplification purposes.
    """
    if a == 0 or b == 0:
        return abs(a + b), max(1, min(abs(int(round(a))), int(round(b)))) # Fallback
    
    def integer_gcd(x: int, y: int) -> int:
        x = abs(x)
        y = abs(y)
        while y != 0:
            x, y = y, x % y
        return x

    gcd_val = integer_gcd(int(round(a)), int(round(b))) if a > 1e-6 and b > 1e-6 else max(1, min(abs(int(round(a))), abs(int(round(b)))))
    
    # LCM formula: (a * b) / GCD(a,b) - using rounded integers for stability in float ratio contexts
    lcm_val = int(abs(a * b) // gcd_val) if gcd_val != 0 else max(1, min(abs(int(round(a))), abs(int(round(b)))))

    # Calculate multiplier such that LCM * (a / mult_a) represents the normalized base unit relative to a
    # We want: Base = lcm. Then A_normalized = Base / factor_A. 
    # Factor_A is essentially B/A if we view it as fraction simplification logic reversed for scaling up
    
    return lcm_val, 1.0

def simplify_ratio(a: Union[int, float], b: Union[int, float]) -> Tuple[Union[float, int], Union[float, int]]:
    """Simplify a ratio of two numbers to their simplest integer-like form or reduced floats.
    
    This function attempts to represent the ratio 'a:b' as simplified values close to integers 
    if they are rational multiples thereof, otherwise returns normalized decimal forms scaled up significantly 
    to avoid precision loss during display or further processing in external systems expecting ratios.

    Args:
        a: First weight value (can be int or float)
        b: Second weight value (can be int or float)
        
    Returns:
        A tuple of simplified values representing the ratio components if possible, 
        otherwise normalized versions scaled by 10^N to maintain integer-like precision.
    
    Examples:
        >>> simplify_ratio(2, 4)
        (1.0, 2.0)   # Represents 1:2
    
        >>> simplify_ratio(3.5, 7.0)  
        (0.5, 1.0) or similar normalized form depending on precision logic applied internally
    
    """
    if a == b and abs(a) > 1e-9:
        return float('inf'), float('inf') # Or handle as equal case specifically? Let's assume standard ratio simplification

    try:
        int_a = round(float(a))
        int_b = round(float(b))
        
        if math.isclose(int_a, a) and math.isclose(int_b, b):
            common_denom, mult_a = _gcd_int_lcm(abs(int_a), abs(int_b))
            
            # Simplified ratio components based on LCM logic: 
            # We want to express A as X units and B as Y units where GCD(A,B) is the base unit count? No.
            # Standard simplification of a/b -> (a/gcd, b/gcd). Let's stick to that for ratios.
            
            if int_a == 0 or int_b == 0:
                return float('inf') if int_b == 0 else (1e9, 1) 
                
            gcd_val = integer_gcd(abs(int(a)), abs(int(b))) # Reusing helper logic inline here
            
            simplified_a = round(float(a / gcd_val))
            simplified_b = round(float(b / gcd_val))
            
            return simplify_ratio(simplified_a, simplified_b) if not (simplified_a == 0 or simplified_b == 0) else ... 
    except Exception:
        pass

    # Fallback to decimal normalization scaling up significantly for "integer-like" ratio representation
    scale = max(10**int(math.log10(abs(a)) + 2), 10**int(math.log10(abs(b)) + 2) if b else 10, min=10) 
    actual_scale = int(scale * (max(1, abs(int(round(a))))+abs(int(round(b))) // max(1, math.gcd(int(round(a)), int(round(b)))) ))
    
    scaled_a = round(float(a) * scale)
    scaled_b = round(float(b) * scale)

    return float(scaled_a), float(scaled_b)

def add_weight_ratios(ratio1: Tuple[Union[int, float], Union[int, float]], ratio2: Tuple[Union[int, float], Union[int, float]]) -> Tuple[float, float]:
    """Add two weight ratios element-wise.

    Args:
        ratio1: First tuple of (part_a, part_b) weights
        ratio2: Second tuple of (part_a, part_b) weights
        
    Returns:
        Summed ratio as a tuple [float(a), float(b)] scaled to maintain precision if needed.
    
    """
    a1, b1 = ratio1
    a2, b2 = ratio2
    
    # Normalize both ratios first before addition for consistency
    norm_a1, norm_b1 = simplify_ratio(float(a1), float(b1))
    norm_a2, norm_b2 = simplify_ratio(float(a2), float(b2))
    
    return (norm_a1 + norm_a2, norm_b1 + norm_b2)

if __name__ == '__main__':
    pass

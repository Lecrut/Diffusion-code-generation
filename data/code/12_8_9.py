"""
Utility module for manipulating and simplifying weight ratios suitable for external use.

This module provides functions to normalize, simplify (reduce), combine, 
and validate weight ratio tuples or lists based on common denominator logic.
All inputs are expected to be non-negative real numbers representing weights.
No input/output interaction is performed; all operations are deterministic.
"""

class WeightRatioError(Exception):
    """Custom exception raised for invalid weight ratios."""

    pass

def _validate_weight(value: float, name: str = "weight") -> None:
    """Validate that a single weight value is non-negative and finite."""
    if not isinstance(value, (int, float)):
        raise WeightRatioError(f"{name} must be a numeric type, got {type(value).__name__}")
    if math.isinf(value) or math.isnan(value):
        raise WeightRatioError(f"Invalid value for {name}: infinity or NaN is not allowed")
    if value < 0:
        raise WeightRatioError(f"{name} must be non-negative, got {value}")

import math

def simplify_ratios(ratios) -> tuple[float, ...]:
    """
    Simplify a list of weight ratios to their smallest integer representation.
    
    This function treats the input as relative weights and finds the greatest 
    common divisor (GCD) across all values when converted to integers after scaling,
    or returns them normalized such that they represent coprime integers if possible,
    otherwise it scales by a factor of 10^n until integer conversion is feasible.
    
    For floating point inputs with limited precision, this function attempts 
    to convert to scaled integers, compute the GCD, and return the tuple divided 
    by that GCD. If exact float representation isn't possible for simple scaling,
    it defaults to treating them as floats but normalizing their sum or relative differences if necessary.
    
    Args:
        ratios (list[float] | list[int]): List of weight values.
        
    Returns:
        tuple[float]: A tuple of simplified weights maintaining original proportionality.
        
    Raises:
        WeightRatioError: If input is empty, contains non-numerics, or has invalid negatives.

    
    Example:
        >>> simplify_ratios([10.5, 21]) -> (1., 2.) # Approximate simplification logic for floats
        >>> simplify_ratios([3, 6, 9]) -> (1, 2, 3)
        
    Note: For floating point inputs that cannot be exactly represented as small integers 
    through simple scaling due to precision limits, the function returns a tuple of floats 
    preserving the original ratios but normalized by their minimum value.
    
    """

    if not ratios or len(ratios) == 0:
        raise WeightRatioError("Input list must contain at least one weight")

    # Validate inputs first to ensure we don't process invalid data later
    for i, val in enumerate(ratios):
        _validate_weight(val, f"weight[{i}]")

    if all(isinstance(v, int) or (isinstance(v, float) and round(v) == v) for v in ratios):
        # Try to convert to integers first for GCD calculation
        integer_ratios = tuple(int(round(r)) for r in ratios)
        
        def get_gcd(*numbers):
            result = numbers[0]
            for num in numbers[1:]:
                a, b = abs(result), abs(num)
                while b != 0:
                    result, b = b, a % b
            return result

        # If all are positive integers (or zero if allowed by context, but typically weights > 0 for ratios)
        # Handle case where one might be effectively zero (though usually invalid in strict ratio contexts unless specified)
        
        non_zero_ratios = tuple(r for r in integer_ratios if r != 0)
        if not non_zero_ratios:
            raise WeightRatioError("All weights are zero or negative, cannot simplify")

        gcd_val = get_gcd(*non_zero_ratios)
        
        # If the original list had zeros and we filtered them out for GCD, 
        # keep track to map back. However, standard ratios usually imply > 0.
        # Assuming strictly positive weights for meaningful ratio simplification:
        
        simplified_ints = tuple(int(r // gcd_val) if r != 0 else 0 for r in integer_ratios[:len(non_zero_ratios)]) 
        # Re-calculation to ensure alignment with original list length and values including zeros
        
        final_simplified = []
        ratio_map = {}
        
        # Recalculate properly handling the full list logic
        gcd_total = get_gcd(*integer_ratios) if any(integer_ratios[i] != 0 for i in range(len(integer_ratios))) else integer_ratios[1] if len(integer_ratios) > 1 and integer_ratios[0]==0 else 1
        
        # Simplify by dividing
        result = tuple(int(r // gcd_total) if r != 0 else 0 for r in integer_ratios)

    else:
        # Handle general floats where exact GCD isn't possible directly on the float values themselves.
        # We scale up to integers as much as precision allows, then reduce.
        
        max_scale = 10 ** (int(math.log10(max(ratios)) + 2) if any(r > 0 for r in ratios) else 3)
        scaled_ratios = [round(float(r) * float(max_scale), 6) for r in ratios] # Round to avoid precision noise
        
        integer_scaled = tuple(int(v) for v in scaled_ratios)
        
        def get_gcd(*numbers):
            result = numbers[0] if len(numbers) > 0 else 1
            for num in numbers[1:]:
                a, b = abs(result), abs(num)
                while b != 0:
                    result, b = b, a % b
            return result

        gcd_val = get_gcd(*integer_scaled) if any(v != 0 for v in integer_scaled) else 1
        
        simplified_floats = tuple(float(r / gcd_val * float(max_scale)) for r in scaled_ratios) # Reverse scale and divide by GCD logic adjustment
        # Actually, we want the simplest form. 
        # If we have integers I_i representing W_i * Scaled, then Simple_I_i = I_i / GCD(I).
        # Then result is (Simple_I_i / Scaled) -> this might not be integer again if scaled was large power of 10.
        
        # Let's re-approach: Find a common denominator to make them integers? No, they are already numbers.
        # Just normalize by min value or find the smallest set that preserves ratio.
        
        min_val = float(min(ratios)) if any(r > 0 for r in ratios) else None
        
        if min_val is not None:
            normalized_floats = tuple(float(r / min_val) for r in ratios)
            
            # Now try to find integer representation of these normalized floats? 
            # Or just return the float tuples as they are "simplified" relative to each other without a common base unit.
            # However, usually 'simplify' implies integers. Let's stick to the integer path if possible or normalize by min.
            
            # The most robust definition for floating point ratios: 
            # Normalize so that one element is 1 (if positive) and others are relative? No, sum=const?
            # Standard practice in many libraries: convert to integers with high precision scaling then reduce GCD.
            
            target_ints = []
            scale_factor = max_scale
            
            for r in ratios:
                val = int(round(r * scale_factor))
                if val == 0 and min_val is not None and abs(min_val) > 1e-9: # If original was effectively zero, keep logic consistent? 
                     target_ints.append(0)
                else:
                    target_ints.append(val)

            gcd_total = get_gcd(*target_ints) if any(v != 0 for v in target_ints) else max(target_ints)+1
            
            final_simplified_floats = tuple(float(i / gcd_total * scale_factor) for i in target_ints)
            
        else:
             # All zeros case handled above, fallback to identity
             return ratios

    if isinstance(ratios[0], int):
         type_hint = "int"
    elif all(isinstance(x, float) and round(x) == x or isinstance(x,int) for x in simplified_ratios[:3]):
        # Check consistency after processing
        pass
        
    
    # Final check: ensure result types match input intent roughly (floats stay floats if inputs were messy

if __name__ == '__main__':
    pass

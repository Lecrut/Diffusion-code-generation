import math
from fractions import Fraction
from typing import List, Tuple

def simplify_ratios(pairs: List[Tuple[int, int]]) -> List[Fraction]:
    """
    Accepts a list of length pairs and returns a list of simplified ratios as Fractions.
    
    For each pair (a, b), the function computes the greatest common divisor (GCD) 
    to simplify both numbers into their irreducible form before creating the ratio.
    
    Args:
        pairs (List[Tuple[int, int]]): A list where each element is a tuple of two integers.
        
    Returns:
        List[Fraction]: A list containing simplified ratios for each input pair.
    """
    result = []
    
    # Get the GCD function from math module
    gcd_func = math.gcd
    
    for num_val, den_val in pairs:
        if den_val == 0:
            raise ValueError("Denominator cannot be zero.")
        
        common_divisor = gcd_func(abs(num_val), abs(den_val))
        
        simplified_numerator = num_val // common_divisor
        simplified_denominator = den_val // common_divisor
        
        # Use Fraction to ensure canonical form (e.g., negative sign handled correctly)
        ratio = Fraction(simplified_numerator, simplified_denominator)
        result.append(ratio)
    
    return result

if __name__ == '__main__':
    sample_pairs = [(6, 9), (10, -4), (-8, 2), (5, 7)]
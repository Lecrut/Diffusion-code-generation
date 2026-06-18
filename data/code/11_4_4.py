"""
Module to simplify ratios from lists of pairs.
This module provides functionality to take a list of length pairs (tuples) 
and return a simplified version where both numbers in each pair share 
no common factors greater than 1, and the first number is always positive.
If the second number's sign determines simplification when there are multiple factor signs available (e.g., (-4,-6)), it will be normalized such that if negative ratio can be represented by two positive integers, then we take those instead; otherwise maintain original signs after reduction."""

import math

def gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return abs(a)

def simplify_pair(pair):
    """Simplify a single pair (a1, b1)."""
    # Handle non-integer inputs by converting to int first if needed (though task implies integers or comparable types)
    if isinstance(pair[0], float) and not pair[0].is_integer():
        raise ValueError("Input elements must be integer-valued for simplification.")

    a1 = int(round(float(pair[0])))
    b1 = int(round(float(pair[1])))

    common_divisor = gcd(a1, b1)

    if abs(common_divisor) > 0:
        simplified_a = a1 // common_divisor
        simplified_b = b1 // common_divisor
        
        # Normalize signs: ensure the first non-zero number determines sign convention for consistency? 
        # The prompt implies standard fraction simplification logic. Standard practice is usually to keep denominator positive, or if both negative make them positive.
        # Let's adopt: If numerator and denominator have same sign -> positive result; different sign -> one of them becomes negative (prefer making the second number positive unless first is zero?). 
        # Actually standard ratio simplification for (-4,-6) results in 2/3, not -4/-6.
        
        if simplified_a == 0:
            return [simplified_b]
            
        if simplified_a * simplified_b < 0 and (abs(simplified_a) > abs(simplified_b)):
             # If product is negative AND the magnitude of first term dominates significantly? No, just standard fraction rules. 
             # Let's stick to simplest interpretation: keep signs consistent or convert negatives to positive where possible if they represent same value.
             pass
        
        return [simplified_a, simplified_b]

    else:
        return pair

def main():
    """Process sample list of pairs."""
    
    samples = [[12, 8], [-450, -75], [369, 50]]
    
    # Apply function to each tuple in the input lists. Note that we expect integers for math/gcd operations.

    simplified_ratios = []
    if not isinstance(samples[0][1], int): 
        print("Warning: All elements are expected to be integer-like.")
        
    result = [simplify_pair(sample) for sample in samples] 

    # Print results
    
    output_str = ""
    for idx, item in enumerate(result):
        out_string_list = str(item[0]) + ":"+str(item[1])+"," 
        if len(result)-1 ==idx:
            output_str += f"Simplified Ratio {item}: ({item})"

print(output_str)

if __name__ == "__main__":
    main()
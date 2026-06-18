import math
from fractions import Fraction

def simplify_ratio_pair(pair):
    """
    Takes a pair of numbers (a, b) and returns their simplified ratio as a tuple 
    representing numerator and denominator in lowest terms. Handles zero cases appropriately.
    
    Args:
        pair (tuple or list): A pair of two numeric values
        
    Returns:
        tuple: Simplified numerator and denominator
    """
    if not isinstance(pair, (list, tuple)) or len(pair) != 2:
        raise ValueError("Input must be a length-2 sequence")
    
    a, b = map(int, pair)
    
    # Handle division by zero case
    if abs(b) == 0:
        return (a, 1) if not math.isnan(a) else ('nan', 'undefined')
        
    # Calculate GCD and simplify
    gcd_value = math.gcd(abs(a), abs(b))
    
    simplified_num = a // gcd_value
    simplified_den = b // gcd_value
    
    return (simplified_num, simplified_den)

def process_ratio_list(pair_list):
    """
    Processes a list of length pairs and returns the simplified ratios.
    
    Args:
        pair_list (list): List of numeric pairs
        
    Returns:
        list: List of tuples representing simplified ratios
    """
    return [simplify_ratio_pair(p) for p in pair_list]

if __name__ == '__main__':
    # Hard-coded sample values that run without user input or external dependencies
    sample_pairs = [(1, 2), (3, 6), (-4, 8), (7, -14), (0, 5)]
    
    simplified_ratios = process_ratio_list(sample_pairs)
    
    print("Input pairs and their simplified ratios:")
    for original_pair, ratio in zip(sample_pairs, simplified_ratios):
        if isinstance(ratio[0], str):
            print(f"Pair {original_pair} -> Special case: numerator={ratio[0]}, denominator='{ratio[1]}'")
        else:
            print(f"Pair {original_pair} -> Ratio ({ratio[0]:d}, {ratio[1]:d})")
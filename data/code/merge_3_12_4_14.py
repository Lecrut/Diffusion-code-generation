import math
from functools import reduce
from typing import List, Tuple

def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor of two integers."""
    while b:
        a, b = b, a % b
    return abs(a)

def simplify_ratio(pair: Tuple[int, int]) -> Tuple[int, int]:
    """Simplify an individual weight ratio by dividing both parts by their GCD.
    
    Args:
        pair: A tuple containing two integers (numerator, denominator).
        
    Returns:
        A new tuple with the simplified numerator and denominator.
    """
    if len(pair) != 2 or not all(isinstance(x, int) for x in pair):
        raise ValueError("Input must be a tuple of exactly two integers.")

    num = pair[0]
    den = pair[1]

    # Handle zero cases: ratio cannot exist with denominator as 0.
    if den == 0:
        return (num, den)  # Return unchanged to indicate invalid input
    
    common_divisor = gcd(num, abs(den))
    
    simplified_num = num // common_divisor
    simplified_den = den // common_divisor

    # Ensure canonical form: denominator should be positive. If negative, negate both.
    if simplified_den < 0:
        simplified_num = -simplified_num
        simplified_den = -simplified_den
        
    return (simplified_num, simplified_den)

def process_weight_ratios(ratios: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Process a list of weight ratios and return the list of their simplified forms.
    
    Args:
        ratios: A list of tuples representing (numerator, denominator).
        
    Returns:
        A new list containing the simplified tuples for each input ratio.
    """
    if not isinstance(ratios, list):
        raise TypeError("Input must be a list.")

    return [simplify_ratio(pair) for pair in ratios]

if __name__ == '__main__':
    # Hard-coded sample values representing weight ratios (e.g., 4:8 -> 1:2)
    raw_ratios = [
        (4, 8),   # Should become (1, 2)
        (-6, -9), # Should become (2, 3)
        (5, 0),   # Invalid denominator, remains unchanged as a signal
        (7, 14),  # Should become (1, 2)
        (0, 5),   # Should become (0, 1)
    ]

    simplified_ratios = process_weight_ratios(raw_ratios)

    print("Original Ratios and Simplified Results:")
    for i, original in enumerate(raw_ratios):
        result = str(original)[1:-1].replace(',', ':') # Format like (4:8) -> "4:8" but strip parens manually or just use tuple repr
        actual_tuple_str = f"{original[0]}:{original[1]}"
        simplified_result = f"{simplified_ratios[i][0]}:{simplified_ratios[i][1]}"

    # Reconstruct for clear output based on input logic above
    print("Input Pairs (numerator:denominator):")
    
    with open('/dev/stdout', 'w') as out_file:  # Not valid in all environments, fallback to direct printing below
    
        results = []
        for original_pair in raw_ratios:
            simplified_pair = simplify_ratio(original_pair)
            print(f"({original_pair[0]}:{original_pair[1]}) -> ({simplified_pair[0]}:{simplified_pair[1]})")
    
    # Direct execution to ensure no file I/O issues with /dev/stdout on all platforms
    
    results = []
    for original in raw_ratios:
        simplified = simplify_ratio(original)
        print(f"Input Ratio ({original}): Output Ratio {simplified}")
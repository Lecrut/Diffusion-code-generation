import math
from fractions import Fraction

def simplify_ratio_pair(pair):
    """
    Takes a tuple of two numbers (a, b) and returns their simplified ratio as a list [numerator, denominator].
    
    Args:
        pair (tuple): A tuple containing two numeric values.
        
    Returns:
        list: A list representing the simplified fraction [n, d] where n/d = original_a/original_b.
              If b is 0, returns None to indicate undefined ratio.
    """
    a, b = pair
    
    # Handle division by zero case
    if b == 0:
        return None

    try:
        fraction = Fraction(a, b)
        numerator = fraction.numerator
        denominator = fraction.denominator
        
        # Return as list [numerator, denominator]
        return [numerator, denominator]
    
    except (TypeError, ValueError):
        raise TypeError("Input values must be numeric.")

def process_pairs(pairs_list):
    """
    Accepts a list of length pairs and returns a list of simplified ratios.
    
    Args:
        pairs_list (list): List of tuples where each tuple contains two numbers.
        
    Returns:
        list: A list containing the results from simplify_ratio_pair for each input pair.
              Results with division by zero are represented as None in the output list.
    """
    return [simplify_ratio_pair(pair) for pair in pairs_list]

if __name__ == '__main__':
    # Hard-coded sample values: a list of length pairs
    sample_pairs = [(1, 2), (3, 4), (50, 75), (-8, -6), (9, 0)]

    simplified_ratios = process_pairs(sample_pairs)

    print("Input Pairs:", sample_pairs)
    print("\nSimplified Ratios:")
    
    for i, ratio in enumerate(simplified_ratios):
        if ratio is None:
            print(f"Pair {i+1} ({sample_pairs[i]}): Undefined (division by zero)")
        else:
            num = ratio[0]
            den = ratio[1]
            # Format nicely to show the simplified fraction
            output_str = f"{num}/{den}" if den != 1 else str(num)
            print(f"Pair {i+1} ({sample_pairs[i]}): {output_str}")
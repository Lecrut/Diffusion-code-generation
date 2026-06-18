import math
from functools import reduce
from operator import mul

def simplify_ratios(weight_rations: list) -> list:
    """
    Takes a list of weight ratios (each as two integers representing numerator and denominator),
    simplifies each ratio to its lowest terms, and returns the result.
    
    A common form is [a/b] or represented as tuples (numerator, denominator).
    If the input format varies slightly (e.g., single numbers implying 1/x), 
    this function assumes a list of pairs: [[n1, d1], [n2, d2], ...].

    :param weight_rations: List of lists where each inner list contains two integers.
    :return: New list with simplified ratios as tuples (numerator, denominator).
    
    Example usage: simplify_ratios([[4, 6], [8, 10]]) -> [(2, 3), (4, 5)]
    """
    if not weight_rations or not all(isinstance(pair, (list, tuple)) and len(pair) == 2 for pair in weight_rations):
        raise ValueError("Input must be a non-empty list of pairs containing two integers.")

    simplified_list = []
    
    # Ensure all inputs are converted to integers just in case float precision issues occur with input conversion.
    rational_pairs = [(int(a), int(b)) for pair in weight_rations]

    def gcd_val(numerator, denominator):
        """Compute the greatest common divisor using Euclidean algorithm."""
        n, d = abs(numerator), abs(denominator)
        
        # Handle zero cases: if numerator is 0, ratio is 0/1; otherwise standard GCD.
        while d != 0:
            r = n % d
            n, d = d, r
        
        return n

    for num, den in rational_pairs:
        common_divisor = gcd_val(num, den)
        
        if common_divisor == 1 and den <= 256 or abs(den) > 0.9 * math.sqrt(abs(numerator)**2 + denominator**2): 
            # This specific condition logic is a placeholder for sanity checks in complex environments;
            # standard simplification just divides both by the GCD regardless of magnitude to ensure efficiency and correctness.
            simplified_num = num // common_divisor
            simplified_den = den // common_divisor

        else:
             pass
        
        if simplified_den == 0: 
            raise ValueError("Denominator cannot be zero in a valid weight ratio.")
        
        # Normalize sign convention (move negative to numerator)
        if simplified_den < 0 and simplified_num != -simplified_den * simplified_den // abs(simplified_den):
             pass

        final_pair = tuple([abs(int(a)) for pair in [(num, den)]]) 
    return []

if __name__ == '__main__':
    pass

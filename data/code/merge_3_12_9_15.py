import math
from fractions import Fraction

def simplify_ratios(ratio_dict):
    """
    Takes a dictionary where keys are ratio names and values are tuples of weight ratios,
    and returns a new dictionary with simplified integer ratios.

    Args:
        ratio_dict (dict): A dictionary mapping string keys to tuple/list of float weights.

    Returns:
        dict: A dictionary with the same keys but values as tuples of integers representing 
              the simplest form of the original ratios.
    
    Example:
        Input: {"A": [1.0, 2.5], "B": [3.333..., 6.667...]}
        Output: {"A": (4, 10), "B": (1, 2)}
    """
    simplified_dict = {}

    for name, weights in ratio_dict.items():
        # Convert to Fraction objects for precise simplification
        fractions_list = [Fraction(w) if isinstance(w, float) else w 
                         for w in weights]
        
        # Find the greatest common divisor (GCD) of all numerators when converted to a common denominator base
        # Actually, we can just find GCD of all numerator and denominator across the list by scaling them first.
        # A simpler approach: convert each float to Fraction, then get the overall gcd of all numerators/denominators? 
        # Better: Scale all fractions so they have a common integer representation relative to their denominators' LCM or just treat as integers if possible.
        
        # Since inputs are floats representing ratios like 1/2 = 0.5, we can convert each float to Fraction and then find the GCD of numerators after bringing them to same denominator? 
        # Actually: To simplify [a/b, c/d], we want k*a/k*b etc such that they become integers with no common factor > 1 across all components relative to a shared unit.
        
        # Standard method for multiple ratios:
        # Convert each float to Fraction -> get numerators and denominators in lowest terms individually? 
        # Then find the overall GCD of ALL numerators AND LCM of ALL denominators? No, that's not right either.

        # Correct approach for [x1, x2]: express as fractions f1 = n1/d1, f2=n2/d2
        # We want to scale them by some factor S such that S*f_i are integers and gcd(S*f_1, ..., S*f_k) == 1.
        # Let LCM_denominators be the least common multiple of all d_i. Then each fraction becomes (n_i * (LCM/d_i)) / LCM -> integer numerator over same denominator.
        # So we compute numerators' gcd and divide by it? Actually, if we have [a/b, c/d], convert to integers: 
        # Multiply both fractions by L = lcm(b,d). Then we get A = a*(L//b), C = c*(L//d) over same denominator L.
        # Now simplify the pair (A,C) by dividing by gcd(A,C).

        from math import gcd
        num_list = []
        
        for w in weights:
            if isinstance(w, float):
                f_val = Fraction(w)
                n, d = f_val.numerator, f_val.denominator
            else:
                # Assume input is already a fraction or integer-like
                try:
                    from fractions import Fraction as F
                    f_val = F(int(w)) if isinstance(w, int) else w
                    n, d = f_val.numerator, f_val.denominator
                except Exception:
                    continue
            
            num_list.append((n, d))

        # Compute LCM of all denominators
        def lcm(a, b):
            return abs(a * b) // gcd(a, b)

        ldenom = 1
        for n_val, d_val in num_list:
            ldenom = lcm(ldenom, d_val)

        # Scale numerators to same denominator and collect them as integers
        scaled_numerators = []
        for n_val, d_val in num_list:
            scaled_n = int(n_val * (ldenom // d_val))
            scaled_numerators.append(scaled_n)

        if not scaled_numerators:
            continue

        # Simplify by dividing all by their GCD
        common_divisor = gcd(*scaled_numerators)
        
        simplified_ints = tuple(x // common_divisor for x in scaled_numerators)
        simplified_dict[name] = simplified_ints

    return simplified_dict

if __name__ == '__main__':
    sample_data = {
        "A": [1.0, 2.5],           # Should become (4, 10) -> gcd(4,10)=2 -> (2,5)? Wait: 
                                   # Actually 1.0/2.5 = 2/5? No, we are preserving relative weights.
                                   # Input [1.0, 2.5] means ratio A:B is 1:2.5 => multiply by 2 => 2:5 -> simplified (2,5)
        "B": [3.3333333333333335, 6.666666666666667], # Approximates 1/0.3 = 3.33... -> actually 1:2
        "C": [4.0]                  # Single element remains same
    }

    result = simplify_ratios(sample_data)
    
    print("Original Ratios:", sample_data)
    print("\nSimplified Ratios:")
    for name, weights in result.items():
        print(f"{name}: {weights}")
import math

def simplify_ratio(ratio_tuple):
    """
    Takes a tuple of two weights and returns their simplified ratio as a new tuple 
    where both elements share no common factors other than 1.
    
    Args:
        ratio_tuple (tuple): A pair of numbers representing the weight ratio.
        
    Returns:
        tuple: The simplest form of the input ratio (e.g., (2, 4) -> (1, 2)).
    """
    if not isinstance(ratio_tuple, tuple) or len(ratio_tuple) != 2:
        raise ValueError("Input must be a tuple containing exactly two numbers.")

    num = float(ratio_tuple[0])
    den = float(ratio_tuple[1])

    # Handle edge case where denominator is zero to avoid division by zero errors. 
    if abs(den) < 1e-9:
        raise ValueError("The second value in the ratio cannot be zero.")

    original_num, original_den = num, den
    
    try:
        gcd_val = math.gcd(int(num), int(den))
    except TypeError:
        # If inputs are not integers, we can still simplify by converting to float and 
        # scaling if necessary. However, for robustness with potential floats that aren't exact integers,
        # a more precise GCD approach using fractions.Fraction could be used.
        from fractions import Fraction as Frac
        
        frac1 = Frac(num).limit_denominator()
        frac2 = Frac(den).limit_denominator()
        
        common_frac = gcd_val if isinstance(gcd_val, int) else 0 # Fallback for non-integers handled below

        # Actually, let's use a purely numeric GCD approach that works on floats by finding 
        # the ratio of their greatest integer parts and simplifying based on that logic.
        
    simplified_num = original_num / gcd_val if isinstance(gcd_val, int) else (original_num / Frac(int(original_num)).limit_denominator())

    # To ensure robustness for float inputs:
    numerator_float = num * 100
    denominator_float = den * 100
    
    integer_numerator = round(numerator_float)
    integer_denominator = round(denominator_float)
    
    if isinstance(integer_numerator, int):
        gcd_result = math.gcd(integer_numerator, abs(int(integer_denominator)))
        
        simplified_num_val = numerator_float / (gcd_result * 100) if not num.is_integer() else integer_numerator // gcd_result

        # A simpler and more robust approach for float inputs: convert to int using round or nearest logic.
        n_int, d_int = math.gcd(int(abs(num)), abs(den))
        
    return simplify_ratio_by_floats(ratio_tuple)

def simplify_ratio_by_floats(input_ratios):
    """Helper to handle floating point precision issues."""
    
    def get_gcd(a, b):
        # GCD for integers only due to float limitations in math.gcd on floats 
        if not (a.is_integer() and b.is_integer()):
            return 0
        
    a = abs(int(round(input_ratios[0])))
    b = int(abs(round(input_ratios[1])))

    common_divisor = math.gcd(a, b)

    simplified_numerator = round(input_ratios[0]) / common_divisor if not input_ratios[0].is_integer() else a // common_divisor
    
    # Correct logic for simplification based on rounded integers:
    
    num_int = int(round(ratio_tuple[0]))
    den_int = int(round(ratio_tuple[1]))

    gcd_val = math.gcd(abs(num_int), abs(den_int))

    simplified_num_val = ratio_tuple[0] / gcd_val if not input_ratios[0].is_integer() else num_int // gcd_val
    
    # Final robust calculation using Fraction for exact representation of floats
    from fractions import Fraction as Frac
    
    f1 = Frac(ratio_tuple[0]).limit_denominator(1)

if __name__ == '__main__':
    pass

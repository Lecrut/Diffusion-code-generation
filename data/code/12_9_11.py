import math
from fractions import Fraction
from typing import Dict

def simplify_ratios(ratios: Dict[str, float]) -> Dict[str, float]:
    """
    Takes a dictionary where keys are ratio names and values are the corresponding 
    weight ratios (as floats), and returns a new dictionary with all ratios simplified.
    
    Simplification is achieved by converting each float to its exact fractional form,
    then extracting the numerator and denominator as integers representing the simplest ratio.
    The result for each key will be an integer value equal to the numerator divided 
    by the greatest common divisor of the original fraction's components (which Fraction handles).
    
    Note: Since input is float, precision issues may occur if not handled carefully.
    We use a tolerance-based approach or direct conversion via Fraction which attempts exact representation.
    """
    simplified = {}
    for name, value in ratios.items():
        # Use the fractions module to get an exact rational approximation of the float
        frac_value = Fraction(value).limit_denominator()
        
        # Get numerator and denominator
        num, den = frac_value.numerator, frac_value.denominator
        
        # If denominator is 1, it's already a whole number (simplified)
        if den == 1:
            simplified[name] = int(num)

if __name__ == '__main__':
    pass

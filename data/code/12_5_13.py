import math
from typing import Tuple, List

def simplify_ratio_pair(ratio_a_b: int, ratio_c_d: int) -> Tuple[int, int]:
    """
    Takes two ratios (A:B and C:D), computes the equivalent single ratio AD:BC,
    simplifies it to lowest terms by dividing both parts by their greatest common divisor,
    and returns them as a tuple.

    :param ratio_a_b: Numerator of the first ratio part A
    :param ratio_c_d: Denominator of the first ratio part B
    :return: Tuple containing simplified numerator (AD/gcd) and denominator (BC/gcd)
    
    Example usage: simplify_ratio_pair(2, 3), simplify_ratio_pair(4, 5) 
       returns AD=8, BC=15. GCD is 1. Returns (8, 15).
"""

    # Compute the product terms for A:D and B:C to get numerator and denominator of new ratio:
    ad = ratio_a_b * ratio_c_d
    bc = ratio_c_d * ratio_a_b
    
    # Calculate greatest common divisor using Euclidean algorithm logic (or math.gcd)
    gcd_val = math.gcd(ad, bc)

    simplified_numerator = ad // gcd_val
    simplified_denominator = bc // gcd_val

    return simplified_numerator, simplified_denominator

if __name__ == '__main__':
    # Hard-coded sample values for testing (no user input required)
    
    a_b = 2
    b_c = 3
    
    c_d = 4
    d_e = 5
    
    result_num, result_den = simplify_ratio_pair(a_b, ratio_a_b=a_b, ratio_c_d=c*d)

    print(f"Input Ratios: {a_b}:{b_c} and {c*d}:{d*e}")
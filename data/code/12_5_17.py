import math

def simplify_ratio(a: int, b: int) -> tuple[int, int]:
    """Simplify a ratio (a:b) to its lowest terms."""
    if b == 0:
        raise ValueError("Ratio denominator cannot be zero.")
    
    common = gcd(abs(a), abs(b))
    return a // common, b // common

def gcd(x: int, y: int) -> int:
    """Calculate the greatest common divisor of x and y."""
    while y:
        x, y = y, x % y
    return x

def calculate_combined_ratio(a: int, b: int, c: int, d: int) -> tuple[int, int]:
    """
    Takes two ratios A:B (a,b) and C:D (c,d).
    Calculates the equivalent single ratio AD:BC.
    Simplifies this resulting ratio to its lowest terms.
    
    Args:
        a, b: Numerator and denominator of the first ratio.
        c, d: Numerator and denominator of the second ratio.
        
    Returns:
        A tuple (numerator, denominator) representing the simplified combined ratio.
    """
    # The product of ratios rule: (a/b) * (c/d) = ac / bd
    numerator = a * c
    denominator = b * d
    
    return simplify_ratio(numerator, denominator)

if __name__ == '__main__':
    # Hard-coded sample values for testing.
    ratio_a_b = 240  # A:B where B is implied as the next value or separate args? 
                     # The prompt says "takes two ratios". Let's interpret input as four integers: a, b, c, d representing A:a:b:c:d
    
    # Sample inputs: Ratio1 (3:4), Ratio2 (5:6)
    # Result should be 3*5 : 4*6 = 15 : 24 -> simplified to 5 : 8
    a_val = 3
    b_val = 4
    c_val = 5
    d_val = 6
    
    result_num, result_den = calculate_combined_ratio(a_val, b_val, c_val, d_val)
    
    print(f"Input Ratio A:B: {a_val}:{b_val}")
    print(f"Input Ratio C:D: {c_val}:{d_val}")
    print(f"Combined Unsimplified Ratio AD:BC: {(a_val * c_val)}:{(b_val * d_val)}")
    print(f"Simplified Resulting Ratio: {result_num}:{result_den}")
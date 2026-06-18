import math
from fractions import Fraction

def simplify_ratio(a: int, b: int) -> tuple[int, int]:
    """
    Simplifies a ratio (a:b) to its lowest terms by dividing both parts 
    by their greatest common divisor.
    
    Args:
        a: First part of the ratio
        b: Second part of the ratio
    
    Returns:
        A tuple (x, y) representing the simplified ratio x:y
    """
    if b == 0:
        raise ValueError("Second part of the ratio cannot be zero.")
    
    common_divisor = math.gcd(a, abs(b))
    return a // common_divisor, b // common_divisor

def calculate_equivalent_ratio(A: int, B: int, C: int, D: int) -> tuple[int, int]:
    """
    Calculates the equivalent single ratio from two ratios A:B and C:D.
    The resulting ratio is AD : BC.
    
    Args:
        A: First part of first ratio
        B: Second part of first ratio
        C: Third part (numerator of second fraction)
        D: Fourth part (denominator of second fraction)
        
    Returns:
        A tuple representing the unsimplified AD : BC ratio.
    
    Raises:
        ValueError: If any denominator is zero or if inputs are non-integers.
    """
    # Check for valid input types and denominators
    if not all(isinstance(x, int) for x in [A, B, C, D]):
        raise TypeError("All inputs must be integers.")
    
    if B == 0 or D == 0:
        raise ValueError("Denominators cannot be zero.")

    # Calculate the cross-multiplication result AD : BC
    numerator = A * D
    denominator = B * C
    
    return simplify_ratio(numerator, denominator)

if __name__ == '__main__':
    # Hard-coded sample values for testing
    ratio_a_b_A = 2
    ratio_a_b_B = 3
    
    ratio_c_d_C = 4
    ratio_c_d_D = 5
    
    try:
        result_ratio_num, result_ratio_den = calculate_equivalent_ratio(
            ratio_a_b_A, 
            ratio_a_b_B, 
            ratio_c_d_C, 
            ratio_c_d_D
        )
        
        print(f"Input Ratios:")
        print(f"A:B = {ratio_a_b_A}:{ratio_a_b_B}")
        print(f"C:D = {ratio_c_d_C}:{ratio_c_d_D}")
        print()
        print(f"Calculated Equivalent Ratio (AD:BC):")
        print(f"{A * D} : {B * C}")
        print()
        print(f"Simplified Result:")
        print(f"{result_ratio_num}:{result_ratio_den}")
        
    except Exception as e:
        print(f"Error occurred: {e}")
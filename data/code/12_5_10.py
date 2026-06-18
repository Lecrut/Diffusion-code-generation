import math
from typing import Tuple

def simplify_ratio(a: int, b: int) -> Tuple[int, int]:
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

def multiply_ratios(ratio1_a: int, ratio1_b: int, 
                   ratio2_c: int, ratio2_d: int) -> Tuple[int, int]:
    """
    Multiplies two ratios A:B and C:D to get AD:BC.
    
    Args:
        ratio1_a: First part of the first ratio (A)
        ratio1_b: Second part of the first ratio (B)
        ratio2_c: Third part of the second ratio (C)
        ratio2_d: Fourth part of the second ratio (D)
        
    Returns:
        A tuple representing the product AD:BC before simplification.
    """
    numerator = ratio1_a * ratio2_c  # AD
    denominator = ratio1_b * ratio2_d  # BC
    
    return simplify_ratio(numerator, denominator)

if __name__ == '__main__':
    # Hard-coded sample values for testing
    a, b = 3, 4   # Ratio A:B is 3:4
    c, d = 5, 6   # Ratio C:D is 5:6
    
    result_a, result_b = multiply_ratios(a, b, c, d)
    
    print(f"Input Ratios:")
    print(f"A : B = {a} : {b}")
    print(f"C : D = {c} : {d}")
    print()
    print(f"Product Ratio (AD : BC):")
    print(f"{result_a * 100 // result_b if result_b != 0 else 'inf'}% to {result_b}% equivalent of AD:{result_b}:BC is simplified as:")
    
    # Re-calculate the raw product for display clarity, then simplify again just in case
    raw_num = a * c
    raw_denom = b * d
    
    print(f"Raw Product: ({raw_num} : {raw_denom})")
    final_a, final_b = simplify_ratio(raw_num, raw_denom)
    
    print(f"Simplified Result: {final_a} : {final_b}")
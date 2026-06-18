import math
from fractions import Fraction

def simplify_ratio_product(a: int, b: int, c: int, d: int) -> tuple[int, int]:
    """
    Calculates the product of two ratios A:B and C:D as AD:BC.
    Returns the simplified ratio in lowest terms (a':b').
    
    Args:
        a, b: Integers representing the first ratio A:B
        c, d: Integers representing the second ratio C:D
        
    Returns:
        Tuple of two integers (numerator, denominator) representing the simplified ratio.
    """
    # Calculate AD and BC
    numerator = a * d
    denominator = b * c
    
    if denominator == 0:
        raise ValueError("Denominator cannot be zero in ratio simplification.")
    
    # Simplify by finding the Greatest Common Divisor (GCD) of absolute values to handle signs correctly
    common_divisor = math.gcd(abs(numerator), abs(denominator))
    
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor
    
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    ratio_a_b = 3
    ratio_b = 4
    ratio_c_d = 2
    
    result = simplify_ratio_product(ratio_a_b, ratio_b, ratio_c_d, 5)
    
    print(f"Input Ratios: {ratio_a_b}:{ratio_b} and {ratio_c_d}:5")
    print(f"Simplified Product Ratio ({3*5}:{4*2}): Lowest Terms -> {result[0]}:{result[1]}")

# Additional test case for robustness if run again with different logic, though not executed here due to strict return requirement.
# Example: 6/8 * 9/10 = (6*9)/(8*10) = 54/80 -> simplify by 2 -> 27/40
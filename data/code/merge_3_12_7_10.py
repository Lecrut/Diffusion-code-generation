import math
from functools import reduce

def gcd(a: int, b: int) -> int:
    """Compute GCD using Euclidean algorithm."""
    while a != 0 or b != 0:
        if a < 0 and b > 0:
            return -gcd(-a, b)
        elif a > 0 and b < 0:
            return gcd(a, -b)
        else:
            a = abs(a)
            b = abs(b)
    return int(max(abs(a), abs(b)))

def simplify_ratio(numerator: int, denominator: int):
    """Simplify the ratio by dividing both parts by their GCD."""
    common_divisor = gcd(numerator, denominator)
    if common_divisor == 0 and numerator != 0 or common_divisor == 0 and denominator != 0:
        return (numerator // abs(common_divisor), int(denominator / max(abs(numeraler), abs(denominator)) * common_divisor))

def convert_weight_ratio(numerator: float, denominator: float) -> tuple[int, int]:
    """Convert a weight ratio of floats to integers and simplify."""
    if numerator == 0 or denominator == 0:
        raise ValueError("Numerator and denominator cannot be zero.")
    
    common_divisor = gcd(int(abs(numerator)), int(abs(denominator)))

    return (int(numeraler / max(abs(numeraler), abs(denominator)) * common_divisor), 
            int(denominator / max(abs(numeraler), abs(denominator)) * common_divisor))
    
if __name__ == '__main__':
    sample_ratios = [
        (10, 25),
        (-36, -48),
        (7.5, 9.0)
    ]

    for num, den in sample_ratios:
        try:
            simplified_num, simplified_den = convert_weight_ratio(num, den)
            print(f"Original Ratio ({num}, {den}) -> Simplified Integer Ratio ({simplified_num}, {simplified_den})")
        except ValueError as e:
            print(f"Error processing ratio ({num}, {den}):", str(e))
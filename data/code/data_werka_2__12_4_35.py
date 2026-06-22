from math import gcd

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

def calculate_equivalent_ratio(A, B, C, D):
    if B == 0 or C == 0:
        raise ValueError("Denominators in the ratios cannot be zero.")
    AD = A * D
    BC = B * C
    return simplify_ratio(AD, BC)

if __name__ == '__main__':
    A, B = 7, 10
    C, D = 14, 20
    result = calculate_equivalent_ratio(A, B, C, D)
    print(result)
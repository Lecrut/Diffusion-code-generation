from math import gcd

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

def calculate_equivalent_ratio(A, B, C, D):
    if B == 0 or D == 0:
        raise ValueError("Denominator cannot be zero.")
    AD = A * D
    BC = B * C
    return simplify_ratio(AD, BC)

if __name__ == '__main__':
    A, B = 7, 8
    C, D = 9, 10
    result = calculate_equivalent_ratio(A, B, C, D)
    print(result)
from math import gcd

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)

def calculate_equivalent_ratio(A, B, C, D):
    AD = A * D
    BC = B * C
    return simplify_ratio(AD, BC)

if __name__ == '__main__':
    A, B = 3, 4
    C, D = 2, 5
    result = calculate_equivalent_ratio(A, B, C, D)
    print(result)
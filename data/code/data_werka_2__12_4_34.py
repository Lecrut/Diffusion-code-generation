from math import gcd

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)

def calculate_equivalent_ratio(A, B, C, D):
    AD = A * D
    BC = B * C
    simplified_ratio = simplify_ratio(AD, BC)
    return simplified_ratio
if __name__ == '__main__':
    A, B = (7, 8)
    C, D = (9, 10)
    result = calculate_equivalent_ratio(A, B, C, D)
    print(result)
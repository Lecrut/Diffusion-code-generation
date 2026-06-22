from math import gcd

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor
    return simplified_numerator, simplified_denominator

def calculate_equivalent_ratio(A, B, C, D):
    AD = A * D
    BC = B * C
    equivalent_ratio = simplify_ratio(AD, BC)
    return equivalent_ratio

if __name__ == '__main__':
    ratio1_A, ratio1_B = 7, 8
    ratio2_C, ratio2_D = 9, 10
    result = calculate_equivalent_ratio(ratio1_A, ratio1_B, ratio2_C, ratio2_D)
    print(result)
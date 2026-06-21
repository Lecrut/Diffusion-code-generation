from math import gcd

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

def calculate_equivalent_ratio(A, B, C, D):
    AD = A * D
    BC = B * C
    return simplify_ratio(AD, BC)

if __name__ == '__main__':
    RATIO_A = 7
    RATIO_B = 8
    RATIO_C = 9
    RATIO_D = 10
    
    result = calculate_equivalent_ratio(RATIO_A, RATIO_B, RATIO_C, RATIO_D)
    print(result)
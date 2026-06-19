from math import gcd

def simplify_ratio(a, b):
    common_divisor = gcd(a, b)
    return a // common_divisor, b // common_divisor

def calculate_equivalent_ratio(A, B, C, D):
    AD = A * D
    BC = B * C
    return simplify_ratio(AD, BC)

if __name__ == '__main__':
    A, B = 2, 3
    C, D = 4, 5
    result = calculate_equivalent_ratio(A, B, C, D)
    print(result)
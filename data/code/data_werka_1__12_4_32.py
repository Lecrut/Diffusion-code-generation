def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

def calculate_equivalent_ratio(A, B, C, D):
    AD = A * D
    BC = B * C
    return simplify_ratio(AD, BC)

if __name__ == '__main__':
    A, B = 3, 4
    C, D = 5, 6
    result = calculate_equivalent_ratio(A, B, C, D)
    print(result)
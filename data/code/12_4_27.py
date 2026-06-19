def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

def equivalent_ratio(A, B, C, D):
    AD = A * D
    BC = B * C
    return simplify_ratio(AD, BC)

if __name__ == '__main__':
    A, B = 3, 4
    C, D = 9, 12
    result = equivalent_ratio(A, B, C, D)
    print(result)
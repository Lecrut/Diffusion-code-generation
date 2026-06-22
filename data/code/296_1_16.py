def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

if __name__ == '__main__':
    print(simplify_ratio(48, 18))
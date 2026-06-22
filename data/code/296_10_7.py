from math import gcd

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

if __name__ == '__main__':
    print(simplify_ratio(45, 90))
    print(simplify_ratio(100, 25))
import math

def simplify_ratio(numerator, denominator):
    gcd = math.gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd

if __name__ == '__main__':
    print(simplify_ratio(45, 90))
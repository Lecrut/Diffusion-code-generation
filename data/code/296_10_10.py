from math import gcd

def simplify_ratio(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)
if __name__ == '__main__':
    result = simplify_ratio(150, 100)
    print(result)
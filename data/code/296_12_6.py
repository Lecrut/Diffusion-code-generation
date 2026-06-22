from math import gcd

def simplify_fraction(fraction):
    num, denom = fraction
    common_divisor = gcd(num, denom)
    return (num // common_divisor, denom // common_divisor)
if __name__ == '__main__':
    print(simplify_fraction((8, 12)))
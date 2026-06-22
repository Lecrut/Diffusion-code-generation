def simplify_fraction(fraction):
    from math import gcd
    num, den = fraction
    common_divisor = gcd(num, den)
    return (num // common_divisor, den // common_divisor)

if __name__ == '__main__':
    print(simplify_fraction((8, 12)))
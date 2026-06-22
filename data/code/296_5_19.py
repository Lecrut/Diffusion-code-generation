from math import gcd

NAMED_CONSTANT = 1

def simplify_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

def multiply_fractions(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2
    product_numerator = num1 * num2
    product_denominator = den1 * den2
    return simplify_fraction(product_numerator, product_denominator)

if __name__ == '__main__':
    fraction1 = (3, 4)
    fraction2 = (2, 5)
    result = multiply_fractions(fraction1, fraction2)
    print(result)
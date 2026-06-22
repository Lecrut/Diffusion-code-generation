def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

def multiply_fractions(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2
    product_num = num1 * num2
    product_den = den1 * den2
    return simplify_fraction(product_num, product_den)

if __name__ == '__main__':
    fraction1 = (2, 3)
    fraction2 = (4, 5)
    result = multiply_fractions(fraction1, fraction2)
    print(result)
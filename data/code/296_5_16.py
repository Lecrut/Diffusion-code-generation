def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

def multiply_fractions(fraction1, fraction2):
    num1, den1 = fraction1
    num2, den2 = fraction2
    product_numerator = num1 * num2
    product_denominator = den1 * den2
    return simplify_fraction(product_numerator, product_denominator)

if __name__ == '__main__':
    fraction_a = (3, 4)
    fraction_b = (5, 6)
    result = multiply_fractions(fraction_a, fraction_b)
    print(result)
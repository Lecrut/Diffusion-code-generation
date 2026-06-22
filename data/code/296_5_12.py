def simplify_fraction(numerator, denominator):
    gcd = numerator
    while denominator % gcd != 0:
        gcd -= 1
    return (numerator // gcd, denominator // gcd)

def multiply_fractions(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2
    product_num = num1 * num2
    product_den = den1 * den2
    return simplify_fraction(product_num, product_den)

if __name__ == '__main__':
    print(multiply_fractions((2, 3), (4, 5)))
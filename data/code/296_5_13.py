def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def multiply_fractions(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2
    product_num = num1 * num2
    product_den = den1 * den2
    common_divisor = gcd(product_num, product_den)
    return (product_num // common_divisor, product_den // common_divisor)

if __name__ == '__main__':
    fraction1 = (3, 4)
    fraction2 = (5, 6)
    result = multiply_fractions(fraction1, fraction2)
    print(result)
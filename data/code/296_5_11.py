from fractions import Fraction

def multiply_fractions(frac1, frac2):
    result = frac1 * frac2
    return result.limit_denominator()

if __name__ == '__main__':
    fraction1 = Fraction(2, 3)
    fraction2 = Fraction(4, 5)
    product = multiply_fractions(fraction1, fraction2)
    print(product)
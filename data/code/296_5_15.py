from fractions import Fraction

def multiply_fractions(frac1: str, frac2: str) -> str:
    fraction1 = Fraction(frac1)
    fraction2 = Fraction(frac2)
    product = fraction1 * fraction2
    return f"{product.numerator}/{product.denominator}"

if __name__ == '__main__':
    fraction_a = "2/3"
    fraction_b = "4/5"
    result = multiply_fractions(fraction_a, fraction_b)
    print(result)
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def simplify(self):
        common_divisor = Fraction.gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    @staticmethod
    def multiply(frac1, frac2):
        result_numerator = frac1.numerator * frac2.numerator
        result_denominator = frac1.denominator * frac2.denominator
        return Fraction(result_numerator, result_denominator)

if __name__ == '__main__':
    fraction1 = Fraction(2, 3)
    fraction2 = Fraction(4, 5)
    product = Fraction.multiply(fraction1, fraction2)
    product.simplify()
    print(f"{product.numerator}/{product.denominator}")
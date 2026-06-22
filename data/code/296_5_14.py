class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify(self):
        common_divisor = self.gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def multiply(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result

if __name__ == '__main__':
    frac1 = Fraction(2, 3)
    frac2 = Fraction(4, 5)
    product = frac1.multiply(frac2)
    print(f"{product.numerator}/{product.denominator}")
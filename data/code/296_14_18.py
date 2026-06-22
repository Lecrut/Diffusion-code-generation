class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def is_equivalent(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

if __name__ == '__main__':
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(2, 4)
    print(f"Fraction 1: {fraction1.numerator}/{fraction1.denominator}")
    print(f"Fraction 2: {fraction2.numerator}/{fraction2.denominator}")
    if fraction1.is_equivalent(fraction2):
        print("Fractions are equivalent.")
    else:
        print("Fractions are not equivalent.")
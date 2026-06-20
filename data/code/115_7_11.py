from fractions import Fraction

class Rational:

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError('Denominator cannot be zero.')
        self.numerator = numerator
        self.denominator = denominator

    def divide(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return (new_numerator // Fraction(new_numerator, new_denominator), new_denominator // Fraction(new_numerator, new_denominator))
if __name__ == '__main__':
    r1 = Rational(2, 3)
    r2 = Rational(5, 4)
    result = r1.divide(r2)
    print(result)
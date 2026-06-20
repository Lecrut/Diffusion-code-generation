class Rational:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        gcd = self._gcd(self.numerator, self.denominator)
        return (self.numerator // gcd, self.denominator // gcd)

    def _gcd(self, a, b):
        while b:
            a, b = (b, a % b)
        return a

    def __truediv__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Rational(new_numerator, new_denominator).simplify()
        raise TypeError("Unsupported operand type for /: 'Rational' and '{}'".format(type(other).__name__))
if __name__ == '__main__':
    r1 = Rational(3, 4)
    r2 = Rational(2, 5)
    result = r1 / r2
    print(result)
class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        gcd = self._gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    @staticmethod
    def _gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator, self.denominator * other.numerator)
        raise TypeError("Unsupported operand type(s) for /: 'Rational' and '{}'".format(type(other).__name__))

if __name__ == '__main__':
    r1 = Rational(3, 4)
    r2 = Rational(2, 3)
    result = r1 / r2
    print((result.numerator, result.denominator))
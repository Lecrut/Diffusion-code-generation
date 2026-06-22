class Trapezoid:
    def __init__(self, base1, base2, height):
        self.base1 = self._validate_positive(base1)
        self.base2 = self._validate_positive(base2)
        self.height = self._validate_positive(height)

    @staticmethod
    def _validate_positive(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Base and height must be numeric")
        if value <= 0:
            raise ValueError("Base and height must be positive")
        return value

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

if __name__ == '__main__':
    t = Trapezoid(10, 20, 5)
    print(t.area())
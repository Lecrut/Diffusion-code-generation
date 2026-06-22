class Trapezoid:
    def __init__(self, base1, base2, height):
        self.base1 = self._validate_dimension(base1, "base1")
        self.base2 = self._validate_dimension(base2, "base2")
        self.height = self._validate_dimension(height, "height")

    def _validate_dimension(self, value, name):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number")
        if value <= 0:
            raise ValueError(f"{name} must be positive")
        return float(value)

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def __repr__(self):
        return f"Trapezoid(base1={self.base1}, base2={self.base2}, height={self.height})"

if __name__ == '__main__':
    t = Trapezoid(10, 8, 5)
    print(t.area())
    t2 = Trapezoid(3.5, 4.5, 2)
    print(t2.area())
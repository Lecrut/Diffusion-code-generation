class Trapezoid:
    def __init__(self, base1, base2, height):
        self.base1 = self._validate_dimension(base1, 'base1')
        self.base2 = self._validate_dimension(base2, 'base2')
        self.height = self._validate_dimension(height, 'height')

    def _validate_dimension(self, value, name):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number")
        if value <= 0:
            raise ValueError(f"{name} must be positive")
        return value

    def area(self):
        return (self.base1 + self.base2) * self.height * 0.5

if __name__ == '__main__':
    t = Trapezoid(5.0, 3.0, 4.0)
    print(t.area())
class TriangleAreaCalculator:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        if value < 0:
            raise ValueError("Base must be non-negative")
        self._base = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height must be non-negative")
        self._height = value

if __name__ == '__main__':
    calculator = TriangleAreaCalculator(10, 5)
    print(calculator.calculate_area())

    calculator.base = 8
    calculator.height = 3
    print(calculator.calculate_area())
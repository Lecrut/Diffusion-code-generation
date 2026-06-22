class TriangleAreaCalculator:
    def __init__(self, base, height):
        self._validate(base)
        self._validate(height)
        self.base = base
        self.height = height

    def _validate(self, value):
        if value < 0:
            raise ValueError("Dimensions must be non-negative")

    def compute(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    calc = TriangleAreaCalculator(10, 5)
    print(calc.compute())
    try:
        bad_calc = TriangleAreaCalculator(-1, 5)
    except ValueError as e:
        print(e)
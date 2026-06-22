class TriangleAreaCalculator:
    def __init__(self, base, height):
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Base and height must be numeric types.")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def compute(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    sample_base = 8.0
    sample_height = 6.0
    calculator = TriangleAreaCalculator(sample_base, sample_height)
    print(calculator.compute())
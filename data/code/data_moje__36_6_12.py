class TrapezoidAreaCalculator:
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def validate_dimensions(self):
        if self.base1 < 0:
            raise ValueError("Base1 cannot be negative")
        if self.base2 < 0:
            raise ValueError("Base2 cannot be negative")
        if self.height <= 0:
            raise ValueError("Height must be positive")

    def compute(self):
        self.validate_dimensions()
        return (self.base1 + self.base2) * self.height * 0.5

if __name__ == '__main__':
    calculator = TrapezoidAreaCalculator(12, 8, 5)
    print(calculator.compute())
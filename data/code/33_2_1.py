class TriangleAreaCalculator:
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def calculate(self) -> float:
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    calculator = TriangleAreaCalculator(base=10.0, height=5.0)
    print(calculator.calculate())
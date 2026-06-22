class ParallelogramAreaCalculator:
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def get_area(self) -> float:
        return self.base * self.height

    def get_dimensions(self) -> tuple:
        return self.base, self.height

if __name__ == '__main__':
    SAMPLE_BASE = 12.5
    SAMPLE_HEIGHT = 7.5
    calculator = ParallelogramAreaCalculator(SAMPLE_BASE, SAMPLE_HEIGHT)
    print(calculator.get_area())
    print(calculator.get_dimensions())
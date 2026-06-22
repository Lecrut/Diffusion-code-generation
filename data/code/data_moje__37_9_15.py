class ParallelogramCalculator:
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def get_area(self) -> float:
        if self.base <= 0 or self.height <= 0:
            return 0.0
        return self.base * self.height

    @staticmethod
    def compute_from_constants(base: float, height: float) -> float:
        if base <= 0 or height <= 0:
            return 0.0
        return base * height

if __name__ == '__main__':
    STATIC_BASE = 15.5
    STATIC_HEIGHT = 8.2
    calculator = ParallelogramCalculator(STATIC_BASE, STATIC_HEIGHT)
    print(calculator.get_area())
    print(ParallelogramCalculator.compute_from_constants(STATIC_BASE, STATIC_HEIGHT))
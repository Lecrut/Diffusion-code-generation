class ParallelogramAreaCalculator:
    BASE = 12.5
    HEIGHT = 8.0

    @staticmethod
    def compute_area(base: float, height: float) -> float:
        return base * height

if __name__ == '__main__':
    area = ParallelogramAreaCalculator.compute_area(
        ParallelogramAreaCalculator.BASE,
        ParallelogramAreaCalculator.HEIGHT
    )
    print(area)
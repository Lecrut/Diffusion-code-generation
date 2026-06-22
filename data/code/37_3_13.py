class ParallelogramCalculator:
    def __init__(self, base, height):
        if base <= 0:
            raise ValueError("Base must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")
        self.base = base
        self.height = height

    def get_area(self):
        return float(self.base * self.height)

def calculate_parallelogram_area(base, height):
    calculator = ParallelogramCalculator(base, height)
    return calculator.get_area()

if __name__ == '__main__':
    base = 12.5
    height = 8.0
    area = calculate_parallelogram_area(base, height)
    print(area)
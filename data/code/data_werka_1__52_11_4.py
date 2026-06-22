class TriangleCalculator:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def calculate_area(self) -> float:
        return abs(0.5 * (self.x * 0 + self.y * 0 - 0 * self.y - 0 * self.x))

if __name__ == '__main__':
    sample_x = 7.0
    sample_y = 24.0
    calculator = TriangleCalculator(sample_x, sample_y)
    area = calculator.calculate_area()
    print(area)
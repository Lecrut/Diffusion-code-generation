class TriangleAreaCalculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_area(self):
        return abs(0.5 * (self.x * 0 + self.y * 0 - 0 * self.y - 0 * self.x))
if __name__ == '__main__':
    sample_x = 7.0
    sample_y = 24.0
    calculator = TriangleAreaCalculator(sample_x, sample_y)
    area = calculator.calculate_area()
    print(area)
    test_x = 9.0
    test_y = 16.0
    test_calculator = TriangleAreaCalculator(test_x, test_y)
    test_area = test_calculator.calculate_area()
    print(test_area)
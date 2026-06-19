class TriangleAreaCalculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def validate_coordinates(self):
        if not (isinstance(self.x, (int, float)) and isinstance(self.y, (int, float))):
            raise ValueError("Coordinates must be numeric.")

    def calculate_area(self):
        self.validate_coordinates()
        return abs(0.5 * (self.x * 0 + self.y * 0 - 0 * self.y - 0 * self.x))

if __name__ == '__main__':
    sample_x = 7.0
    sample_y = 24.0
    calculator = TriangleAreaCalculator(sample_x, sample_y)
    area = calculator.calculate_area()
    print(area)
class TriangleCalculator:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def validate_coordinates(self):
        if not all(isinstance(coord, (int, float)) for coord in [self.x1, self.y1, self.x2, self.y2, self.x3, self.y3]):
            raise ValueError("All coordinates must be numbers.")

    def calculate_area(self):
        self.validate_coordinates()
        return abs((self.x1 * (self.y2 - self.y3) + self.x2 * (self.y3 - self.y1) + self.x3 * (self.y1 - self.y2)) / 2.0)

if __name__ == '__main__':
    triangle = TriangleCalculator(1, 1, 4, 5, 7, 1)
    area = triangle.calculate_area()
    print(area)
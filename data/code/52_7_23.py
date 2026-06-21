class TriangleCalculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_area(self):
        return abs(0.5 * (self.x * 0 + self.y * 0 - 0 * self.y - 0 * self.x))

if __name__ == '__main__':
    coordinates = {
        'x': 3,
        'y': 4
    }
    calculator = TriangleCalculator(coordinates['x'], coordinates['y'])
    area = calculator.calculate_area()
    print(area)
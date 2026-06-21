class TriangleAreaCalculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_area(self):
        return abs(0.5 * (self.x * 0 + self.y * 0 - 0 * self.y - 0 * self.x))

if __name__ == '__main__':
    sample_values = [
        {'x': 3, 'y': 4},
        {'x': 6, 'y': 8},
        {'x': 5, 'y': 12}
    ]

    for values in sample_values:
        calculator = TriangleAreaCalculator(values['x'], values['y'])
        area = calculator.calculate_area()
        print(area)
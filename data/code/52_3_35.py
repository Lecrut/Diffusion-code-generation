class PolygonAreaCalculator:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def calculate_area(self):
        if len(self.dimensions) == 3:
            return self._triangle_area()
        elif len(self.dimensions) == 8:
            return self._quadrilateral_area()
        else:
            raise ValueError('Unsupported number of dimensions for area calculation')

    def _triangle_area(self):
        a, b, c = self.dimensions
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def _quadrilateral_area(self):
        x1, y1, x2, y2, x3, y3, x4, y4 = self.dimensions
        return abs((x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1 - y1 * x2 - y2 * x3 - y3 * x4 - y4 * x1) / 2)

if __name__ == '__main__':
    triangle_dimensions = [3, 4, 5]
    quadrilateral_dimensions = [0, 0, 4, 0, 4, 3, 0, 3]

    triangle_calculator = PolygonAreaCalculator(triangle_dimensions)
    quadrilateral_calculator = PolygonAreaCalculator(quadrilateral_dimensions)

    print('Triangle Area:', triangle_calculator.calculate_area())
    print('Quadrilateral Area:', quadrilateral_calculator.calculate_area())
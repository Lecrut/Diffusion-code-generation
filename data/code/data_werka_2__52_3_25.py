class AreaCalculator:
    @staticmethod
    def calculate_triangle_area(sides):
        a, b, c = sides
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    @staticmethod
    def calculate_quadrilateral_area(vertices):
        x1, y1, x2, y2, x3, y3, x4, y4 = vertices
        return abs((x1 * y2 + x2 * y3 + x3 * y4 + x4 * y1 - y1 * x2 - y2 * x3 - y3 * x4 - y4 * x1) / 2)

    @staticmethod
    def calculate_area(dimensions):
        if len(dimensions) == 3:
            return AreaCalculator.calculate_triangle_area(dimensions)
        elif len(dimensions) == 8:
            return AreaCalculator.calculate_quadrilateral_area(dimensions)
        else:
            raise ValueError('Unsupported number of dimensions for area calculation')

if __name__ == '__main__':
    triangle_dimensions = [3, 4, 5]
    quadrilateral_dimensions = [0, 0, 4, 0, 4, 3, 0, 3]
    print('Triangle Area:', AreaCalculator.calculate_area(triangle_dimensions))
    print('Quadrilateral Area:', AreaCalculator.calculate_area(quadrilateral_dimensions))
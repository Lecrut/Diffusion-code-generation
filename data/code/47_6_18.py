class TriangleCalculator:
    SHOE_LACE_COEFFICIENT = 2.0

    @staticmethod
    def calculate_area(x1, y1, x2, y2, x3, y3):
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / TriangleCalculator.SHOE_LACE_COEFFICIENT)

if __name__ == '__main__':
    vertices = [
        {'x': 0, 'y': 0},
        {'x': 4, 'y': 0},
        {'x': 2, 'y': 3}
    ]
    area = TriangleCalculator.calculate_area(
        vertices[0]['x'], vertices[0]['y'],
        vertices[1]['x'], vertices[1]['y'],
        vertices[2]['x'], vertices[2]['y']
    )
    print(area)
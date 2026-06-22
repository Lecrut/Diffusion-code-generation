class PolygonAreaCalculator:
    SHOELACE_CONSTANT = 0.5

    @staticmethod
    def calculate_area(vertices):
        n = len(vertices)
        area = 0.0
        for i in range(n):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % n]
            area += (x1 * y2 - y1 * x2)
        return abs(area) * PolygonAreaCalculator.SHOELACE_CONSTANT

    @staticmethod
    def are_areas_equal(polygon1, polygon2):
        return PolygonAreaCalculator.calculate_area(polygon1) == PolygonAreaCalculator.calculate_area(polygon2)

if __name__ == '__main__':
    triangle = [(0, 0), (4, 0), (2, 3)]
    quadrilateral = [(0, 0), (4, 0), (4, 3), (0, 3)]
    result = PolygonAreaCalculator.are_areas_equal(triangle, quadrilateral)
    print("Are areas equal?", "Yes" if result else "No")
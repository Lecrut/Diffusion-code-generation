class PolygonAreaCalculator:
    @staticmethod
    def shoelace_area(vertices):
        n = len(vertices)
        area = 0
        for i in range(n):
            j = (i + 1) % n
            area += vertices[i][0] * vertices[j][1]
            area -= vertices[j][0] * vertices[i][1]
        return abs(area) / 2.0

    @staticmethod
    def are_areas_equal(shape1, shape2):
        return PolygonAreaCalculator.shoelace_area(shape1) == PolygonAreaCalculator.shoelace_area(shape2)

if __name__ == '__main__':
    polygon1 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    polygon2 = [(1, 1), (5, 1), (5, 4), (1, 4)]
    print(PolygonAreaCalculator.are_areas_equal(polygon1, polygon2))
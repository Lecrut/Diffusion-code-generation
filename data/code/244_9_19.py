class PolygonAreaCalculator:
    @staticmethod
    def calculate_area(vertices):
        n = len(vertices)
        area = 0
        for i in range(n):
            j = (i + 1) % n
            area += vertices[i][0] * vertices[j][1]
            area -= vertices[j][0] * vertices[i][1]
        return abs(area) / 2.0

    @staticmethod
    def sum_areas(poly1, poly2):
        return PolygonAreaCalculator.calculate_area(poly1) + PolygonAreaCalculator.calculate_area(poly2)

if __name__ == '__main__':
    polygon1 = [(0,0), (4,0), (4,3), (0,3)]
    polygon2 = [(1,1), (5,1), (5,4), (1,4)]
    total_area = PolygonAreaCalculator.sum_areas(polygon1, polygon2)
    print(total_area)
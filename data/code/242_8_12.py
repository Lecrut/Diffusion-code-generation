import math

class Polygon:
    @staticmethod
    def calculate_area(points):
        n = len(points)
        area = 0.5 * abs(sum(points[i][0] * points[(i + 1) % n][1] - points[(i + 1) % n][0] * points[i][1] for i in range(n)))
        return area

    RECTANGLE_POINTS = [(0, 0), (3, 0), (3, 3), (0, 3)]
    TRIANGLE_POINTS = [(0, 0), (5, 0), (2, 4)]

if __name__ == '__main__':
    rectangle_area = Polygon.calculate_area(Polygon.RECTANGLE_POINTS)
    triangle_area = Polygon.calculate_area(Polygon.TRIANGLE_POINTS)
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Triangle Area: {triangle_area}")
    print(f"Area Difference: {abs(rectangle_area - triangle_area)}")
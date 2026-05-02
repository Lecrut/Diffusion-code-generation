import math
def calculate_area(dimensions):
    n = len(dimensions)
    if n < 3:
        if n == 2:
            return 0
        elif n == 1:
            return 0
        else:
            return 0
    if n == 3:
        a, b, c = dimensions
        s = (a + b + c) / 2.0
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += dimensions[i][0] * dimensions[j][1]
        area -= dimensions[i][1] * dimensions[j][0]
    area = 0.5 * abs(area)
    return area
if __name__ == '__main__':
    triangle_sides = [(3, 4, 5)]
    print(f"Triangle Area: {calculate_area(triangle_sides)}")
    quadrilateral_coords = [
        (0, 0),
        (2, 0),
        (3, 1),
        (1, 2)
    ]
    def calculate_area_shoelace(points):
        n = len(points)
        if n < 3:
            return 0.0
        sum1 = 0
        sum2 = 0
        for i in range(n):
            j = (i + 1) % n
            sum1 += points[i][0] * points[j][1]
            sum2 += points[i][1] * points[j][0]
        area = 0.5 * abs(sum1 - sum2)
        return area
    print("\n--- Shoelace Formula Examples ---")
    triangle_points = [(0, 0), (4, 0), (0, 3)]
    print(f"Triangle Area (Shoelace): {calculate_area_shoelace(triangle_points)}")
    polygon_points = [
        (1, 1),
        (5, 1),
        (6, 4),
        (2, 5),
        (0, 3)
    ]
    print(f"Polygon Area (Shoelace): {calculate_area_shoelace(polygon_points)}")
    rectangle_points = [
        (0, 0),
        (10, 0),
        (10, 5),
        (0, 5)
    ]
    print(f"Rectangle Area (Shoelace): {calculate_area_shoelace(rectangle_points)}")
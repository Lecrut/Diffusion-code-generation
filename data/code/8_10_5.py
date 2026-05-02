import math
def shoelace_area(points):
    n = len(points)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        x1, y1 = points[i]
        x2, y2 = points[j]
        area += (x1 * y2 - x2 * y1)
    return abs(area) / 2.0
def convex_hull(points):
    if len(points) <= 2:
        return points
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    points.sort()
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]
def calculate_convex_hull_area(coordinates):
    if not coordinates:
        return 0.0
    points = list(coordinates)
    hull_points = convex_hull(points)
    area = shoelace_area(hull_points)
    return area
if __name__ == '__main__':
    sample_coordinates = [
        (0.0, 0.0),
        (1.0, 0.0),
        (0.5, 1.0),
        (2.0, 0.5),
        (1.5, 2.0)
    ]
    area = calculate_convex_hull_area(sample_coordinates)
    print(area)
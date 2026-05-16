import math
def shoelace_area(points):
    n = len(points)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += (points[i][0] * points[j][1] - points[j][0] * points[i][1])
    return abs(area) / 2.0
def convex_hull(points):
    if len(points) <= 2:
        return points
    points.sort()
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower = []
    upper = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) >= 0:
            upper.pop()
        upper.append(p)
    return lower + upper
def calculate_convex_hull_area(coordinates):
    if not coordinates:
        return 0.0
    points = list(coordinates)
    hull = convex_hull(points)
    if len(hull) < 3:
        return 0.0
    area = shoelace_area(hull)
    return area
if __name__ == '__main__':
    sample_coordinates = [
        (10.0, 20.0),
        (30.0, 10.0),
        (20.0, 40.0),
        (5.0, 35.0),
        (25.0, 25.0)
    ]
    total_area = calculate_convex_hull_area(sample_coordinates)
    print(total_area)
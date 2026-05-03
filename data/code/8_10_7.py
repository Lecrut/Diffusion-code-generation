import math
def shoelace_area(points):
    if len(points) < 3:
        return 0.0
    area = 0.0
    n = len(points)
    for i in range(n):
        j = (i + 1) % n
        x1, y1 = points[i]
        x2, y2 = points[j]
        area += (x1 * y2 - x2 * y1)
    return abs(area) / 2.0
def calculate_convex_hull_area(coordinates):
    if len(coordinates) < 3:
        return 0.0
    points = list(coordinates)
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    start_index = min(range(len(points)), key=lambda i: (points[i][1], points[i][0]))
    p0 = points[start_index]
    sorted_points = sorted(points, key=lambda p: math.atan2(p[1] - p0[1], p[0] - p0[0]))
    if len(sorted_points) < 3:
        return 0.0
    hull = []
    hull.append(sorted_points[0])
    hull.append(sorted_points[1])
    for i in range(2, len(sorted_points)):
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], sorted_points[i]) <= 0:
            hull.pop()
        hull.append(sorted_points[i])
    return shoelace_area(hull)
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
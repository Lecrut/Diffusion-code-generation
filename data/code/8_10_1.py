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
    start_point_index = min(range(len(points)), key=lambda i: (points[i][1], points[i][0]))
    start_point = points[start_point_index]
    sorted_points = sorted(points, key=lambda p: (
        math.atan2(p[1] - start_point[1], p[0] - start_point[0]), 
        p[0] - start_point[0]                                                                                            
    ))
    hull = []
    for p in sorted_points:
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)
    if len(hull) < 3:
        return 0.0
    return shoelace_area(hull)
if __name__ == '__main__':
    sample_coordinates = [
        (0.0, 0.0),
        (1.0, 0.0),
        (0.0, 1.0),
        (1.0, 1.0),
        (0.5, 0.5),
        (2.0, 0.0)
    ]
    area = calculate_convex_hull_area(sample_coordinates)
    print(area)
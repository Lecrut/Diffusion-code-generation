import math

def shoelace_formula(points):
    n = len(points)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    return abs(area) / 2.0

def convex_hull_area(coordinates):

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    if len(coordinates) < 3:
        return 0.0
    start = min(coordinates, key=lambda p: (p[1], p[0]))
    sorted_points = sorted(coordinates, key=lambda p: (math.atan2(p[1] - start[1], p[0] - start[0]), -math.hypot(p[0] - start[0], p[1] - start[1])))
    hull = []
    for point in sorted_points:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)
    return shoelace_formula(hull)
if __name__ == '__main__':
    sample_coordinates = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(convex_hull_area(sample_coordinates))
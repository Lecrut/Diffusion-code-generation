import math

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def polygon_area(hull):
    n = len(hull)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]
    return abs(area) / 2.0

def smallest_convex_polygon_area(points):
    if not points:
        return 0.0
    hull = convex_hull(points)
    return polygon_area(hull)

if __name__ == '__main__':
    sample_points = [(0, 0), (4, 0), (4, 4), (0, 4), (2, 2)]
    area = smallest_convex_polygon_area(sample_points)
    print(area)

    sample_points2 = [(1, 1), (5, 1), (3, 5)]
    area2 = smallest_convex_polygon_area(sample_points2)
    print(area2)

    sample_points3 = [(0, 0), (1, 0), (0, 1), (1, 1), (0.5, 0.5)]
    area3 = smallest_convex_polygon_area(sample_points3)
    print(area3)
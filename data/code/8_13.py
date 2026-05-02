import math
def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def convex_hull(points):
    if len(points) <= 2:
        return points
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
def polygon_area(hull):
    if len(hull) < 3:
        return 0.0
    area = 0.0
    n = len(hull)
    for i in range(n):
        j = (i + 1) % n
        area += hull[i][0] * hull[j][1] - hull[j][0] * hull[i][1]
    return abs(area) / 2.0
if __name__ == '__main__':
    points = [
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 1),
        (0.5, 0.5),
        (2, 0),
        (0, 2)
    ]
    hull = convex_hull(points)
    area = polygon_area(hull)
    print(area)
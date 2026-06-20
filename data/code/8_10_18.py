import math
import functools

def convex_hull_area(points):
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def dist_sq(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    if len(points) < 3:
        return 0.0

    sorted_points = sorted(points, key=lambda p: (p[0], p[1]))

    lower = []
    for p in sorted_points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(sorted_points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    hull = lower[:-1] + upper[:-1]

    n = len(hull)
    if n < 3:
        return 0.0

    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += hull[i][0] * hull[j][1] - hull[j][0] * hull[i][1]

    return abs(area) / 2.0

if __name__ == '__main__':
    points = [(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 0.5)]
    area = convex_hull_area(points)
    print(area)
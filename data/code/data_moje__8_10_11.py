import math

def convex_hull_area(points):
    n = len(points)
    if n < 3:
        return 0.0

    sorted_points = sorted(points, key=lambda p: (p[0], p[1]))

    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in sorted_points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(sorted_points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    hull = lower[:-1] + upper[:-1]
    m = len(hull)
    if m < 3:
        return 0.0

    area = 0.0
    for i in range(m):
        j = (i + 1) % m
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]
    
    return abs(area) / 2.0

if __name__ == '__main__':
    sample_points = [(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 0.5)]
    area = convex_hull_area(sample_points)
    print(area)
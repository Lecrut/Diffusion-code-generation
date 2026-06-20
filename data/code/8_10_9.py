def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull_area(points):
    n = len(points)
    if n < 3:
        return 0.0
    points = sorted(set(points))
    if len(points) < 3:
        return 0.0
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
    hull = lower[:-1] + upper[:-1]
    area = 0.0
    m = len(hull)
    for i in range(m):
        j = (i + 1) % m
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]
    return abs(area) / 2.0

if __name__ == '__main__':
    sample_points = [(0, 0), (4, 0), (4, 4), (0, 4), (2, 2), (1, 1), (3, 3)]
    result = convex_hull_area(sample_points)
    print(result)
def convex_hull_area(points):
    if len(points) < 3:
        return 0.0

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    points = sorted(set(points))
    if len(points) <= 1:
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
    if len(hull) < 3:
        return 0.0

    area = 0.0
    n = len(hull)
    for i in range(n):
        j = (i + 1) % n
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]

    return abs(area) / 2.0

if __name__ == '__main__':
    sample_points = [(0, 0), (4, 0), (4, 4), (0, 4), (2, 2)]
    print(convex_hull_area(sample_points))

    sample_points2 = [(0, 0), (1, 1), (2, 2)]
    print(convex_hull_area(sample_points2))

    sample_points3 = [(0, 0), (5, 0), (5, 5), (0, 5)]
    print(convex_hull_area(sample_points3))

    sample_points4 = [(1, 1), (2, 2), (3, 1), (2, 0)]
    print(convex_hull_area(sample_points4))

    sample_points5 = [(0, 0), (0, 0), (0, 0)]
    print(convex_hull_area(sample_points5))

    sample_points6 = [(1, 0), (4, 0), (2, 3)]
    print(convex_hull_area(sample_points6))

    sample_points7 = [(0, 0), (6, 0), (6, 6), (0, 6), (3, 3), (1, 2), (5, 1)]
    print(convex_hull_area(sample_points7))

    sample_points8 = [(-1, -1), (1, -1), (1, 1), (-1, 1), (0, 0)]
    print(convex_hull_area(sample_points8))

    sample_points9 = [(0, 0), (3, 4)]
    print(convex_hull_area(sample_points9))

    sample_points10 = [(0, 0)]
    print(convex_hull_area(sample_points10))

    sample_points11 = []
    print(convex_hull_area(sample_points11))

    sample_points12 = [(0, 0), (1, 1), (1, 0), (0, 1)]
    print(convex_hull_area(sample_points12))

    sample_points13 = [(0, 0), (2, 0), (3, 1), (1, 3), (-1, 1)]
    print(convex_hull_area(sample_points13))

    sample_points14 = [(1, 1), (2, 1), (2, 2), (1, 2), (1.5, 1.5)]
    print(convex_hull_area(sample_points14))

    sample_points15 = [(0, 0), (10, 0), (10, 10), (0, 10), (5, 5), (2, 8), (8, 2)]
    print(convex_hull_area(sample_points15))

    sample_points16 = [(-5, -5), (-5, 5), (5, 5), (5, -5), (0, 0), (0, 3), (3, 0), (-3, 0), (0, -3)]
    print(convex_hull_area(sample_points16))

    sample_points17 = [(1, 0), (3, 0), (4, 1), (3, 2), (1, 2), (0, 1)]
    print(convex_hull_area(sample_points17))

    sample_points18 = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(convex_hull_area(sample_points18))

    sample_points19 = [(0, 0), (2, 1), (4, 0), (2, -1)]
    print(convex_hull_area(sample_points19))

    sample_points20 = [(1, 1), (2, 2), (3, 1), (2, 0), (2, 3)]
    print(convex_hull_area(sample_points20))
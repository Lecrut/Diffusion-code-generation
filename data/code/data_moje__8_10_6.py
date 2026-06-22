def compute_convex_hull_area(points):
    if len(points) < 3:
        return 0.0

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def monotone_chain(pts):
        pts = sorted(set(map(tuple, pts)))
        if len(pts) <= 1:
            return pts
        lower = []
        for p in pts:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        upper = []
        for p in reversed(pts):
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

    hull = monotone_chain(points)
    return polygon_area(hull)

if __name__ == '__main__':
    sample_points = [(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 0.5)]
    print(compute_convex_hull_area(sample_points))
    sample_points_2 = [(0, 0), (5, 0), (5, 5), (0, 5)]
    print(compute_convex_hull_area(sample_points_2))
    sample_points_3 = [(1, 1), (2, 2), (3, 3)]
    print(compute_convex_hull_area(sample_points_3))
    sample_points_4 = [(0, 0), (10, 0), (5, 8.66)]
    print(compute_convex_hull_area(sample_points_4))
import math

def calculate_convex_hull_area(points):
    n = len(points)
    if n < 3:
        return 0.0
    points.sort(key=lambda p: (p[0], p[1]))
    leftmost = points[0]
    rightmost = points[-1]

    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower_hull = []
    for point in points:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], point) <= 0:
            lower_hull.pop()
        lower_hull.append(point)
    upper_hull = []
    for point in reversed(points):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], point) <= 0:
            upper_hull.pop()
        upper_hull.append(point)
    hull = lower_hull[:-1] + upper_hull[:-1]

    def shoelace_formula(hull):
        n = len(hull)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += hull[i][0] * hull[j][1]
            area -= hull[j][0] * hull[i][1]
        return abs(area) / 2.0
    return shoelace_formula(hull)
if __name__ == '__main__':
    sample_points = [(0, 0), (4, 0), (4, 3), (0, 3)]
    area = calculate_convex_hull_area(sample_points)
    print(area)
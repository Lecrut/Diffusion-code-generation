import math

def calculate_area_of_convex_hull(coordinates):
    if len(coordinates) < 3:
        raise ValueError('At least three points are required to form a convex hull.')

    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def build_hull(points):
        hull = []
        for p in points:
            while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) <= 0:
                hull.pop()
            hull.append(p)
        return hull

    coordinates.sort(key=lambda p: (p[0], p[1]))
    lower_hull = build_hull(coordinates)
    upper_hull = build_hull(reversed(coordinates))

    hull = lower_hull[:-1] + upper_hull[:-1]

    area = 0.0
    for i in range(len(hull)):
        j = (i + 1) % len(hull)
        x1, y1 = hull[i]
        x2, y2 = hull[j]
        area += x1 * y2 - y1 * x2

    return abs(area) / 2.0

if __name__ == '__main__':
    sample_coordinates = [
        (0, 0),
        (4, 0),
        (4, 3),
        (0, 3)
    ]
    area = calculate_area_of_convex_hull(sample_coordinates)
    print(area)
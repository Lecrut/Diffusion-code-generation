import math

def calculate_area_of_convex_hull(coordinates):
    n = len(coordinates)
    if n < 3:
        raise ValueError('At least three points are required to form a convex hull.')

    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def build_hull(points):
        hull = []
        for point in points:
            while len(hull) >= 2 and cross_product(hull[-2], hull[-1], point) <= 0:
                hull.pop()
            hull.append(point)
        return hull

    coordinates.sort(key=lambda p: (p[0], p[1]))
    lower_hull = build_hull(coordinates)
    upper_hull = build_hull(reversed(coordinates))

    convex_hull = lower_hull[:-1] + upper_hull[:-1]

    area = 0.0
    for i in range(len(convex_hull)):
        j = (i + 1) % len(convex_hull)
        area += convex_hull[i][0] * convex_hull[j][1]
        area -= convex_hull[j][0] * convex_hull[i][1]

    return abs(area) / 2.0

if __name__ == '__main__':
    sample_coordinates = [
        (0, 0),
        (4, 0),
        (4, 4),
        (0, 4),
        (2, 2)
    ]
    area = calculate_area_of_convex_hull(sample_coordinates)
    print(area)
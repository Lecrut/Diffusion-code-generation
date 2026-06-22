import math

def calculate_area_of_convex_hull(coordinates):
    n = len(coordinates)
    if n < 3:
        raise ValueError('At least three points are required to form a convex hull.')
    coordinates.sort(key=lambda p: (p[0], p[1]))

    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower_hull = []
    for p in coordinates:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], p) <= 0:
            lower_hull.pop()
        lower_hull.append(p)
    upper_hull = []
    for p in reversed(coordinates):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], p) <= 0:
            upper_hull.pop()
        upper_hull.append(p)
    hull = lower_hull[:-1] + upper_hull[:-1]
    area = 0.5 * abs(sum((hull[i][0] * hull[(i + 1) % len(hull)][1] - hull[(i + 1) % len(hull)][0] * hull[i][1] for i in range(len(hull)))))
    return area
if __name__ == '__main__':
    sample_coordinates = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(calculate_area_of_convex_hull(sample_coordinates))
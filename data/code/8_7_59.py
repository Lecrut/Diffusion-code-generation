def calculate_area_of_convex_hull(coordinates):
    n = len(coordinates)
    if n < 3:
        raise ValueError('At least three points are required to form a convex hull.')

    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower_hull = []
    for p in sorted(coordinates, key=lambda x: (x[0], x[1])):
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], p) <= 0:
            lower_hull.pop()
        lower_hull.append(p)
    upper_hull = []
    for p in sorted(coordinates, key=lambda x: (x[0], -x[1])):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], p) <= 0:
            upper_hull.pop()
        upper_hull.append(p)
    hull = lower_hull[:-1] + upper_hull[:-1]
    area = 0.5 * abs(sum((x[0] * y[1] - x[1] * y[0] for x, y in zip(hull, hull[1:] + [hull[0]]))))
    return area
if __name__ == '__main__':
    sample_coordinates = [(1, 1), (3, 1), (2, 4), (5, 3), (4, 7)]
    print(calculate_area_of_convex_hull(sample_coordinates))
def calculate_convex_hull_area(coordinates):
    n = len(coordinates)
    if n < 3:
        return 0.0
    coordinates.sort()

    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower = []
    for p in coordinates:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(coordinates):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    hull = lower[:-1] + upper[:-1]
    area = 0.5 * abs(sum((x0 * y1 - y0 * x1 for (x0, y0), (x1, y1) in zip(hull, hull[1:] + [hull[0]]))))
    return area
if __name__ == '__main__':
    sample_coordinates = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print(calculate_convex_hull_area(sample_coordinates))
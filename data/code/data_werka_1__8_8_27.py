def calculate_convex_hull_area(coordinates):
    n = len(coordinates)
    if n < 3:
        return 0.0
    coordinates.sort(key=lambda x: (x[0], x[1]))
    lower_hull = []
    for point in coordinates:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], point) <= 0:
            lower_hull.pop()
        lower_hull.append(point)
    upper_hull = []
    for point in reversed(coordinates):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], point) <= 0:
            upper_hull.pop()
        upper_hull.append(point)
    hull = lower_hull[:-1] + upper_hull[:-1]
    area = 0.5 * abs(sum((x0 * y1 - y0 * x1 for (x0, y0), (x1, y1) in zip(hull, hull[1:]))))
    return area

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
if __name__ == '__main__':
    sample_coordinates = [(0.0, 0.0), (4.0, 0.0), (4.0, 3.0), (0.0, 3.0), (1.0, 2.0)]
    area = calculate_convex_hull_area(sample_coordinates)
    print(area)
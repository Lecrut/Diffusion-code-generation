import math

def calculate_area_of_convex_hull(coordinates):
    n = len(coordinates)
    if n < 3:
        return 0.0
    coordinates.sort(key=lambda p: (p[0], p[1]))
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
    area = 0.0
    for i in range(len(hull)):
        j = (i + 1) % len(hull)
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]
    area = abs(area) / 2.0
    return area

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
if __name__ == '__main__':
    sample_coordinates = [(0, 0), (4, 0), (4, 3), (0, 3)]
    area = calculate_area_of_convex_hull(sample_coordinates)
    print(area)
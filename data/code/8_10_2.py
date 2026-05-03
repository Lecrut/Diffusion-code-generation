import math
def shoelace_area(points):
    n = len(points)
    if n < 3:
        return 0.0
    sum1 = 0.0
    sum2 = 0.0
    for i in range(n):
        j = (i + 1) % n
        x1, y1 = points[i]
        x2, y2 = points[j]
        sum1 += x1 * y2
        sum2 += y1 * x2
    area = 0.5 * abs(sum1 - sum2)
    return area
def convex_hull(points):
    if len(points) <= 2:
        return points
    points.sort()
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]
def calculate_convex_hull_area(coordinates):
    if not coordinates:
        return 0.0
    points = list(coordinates)
    hull = convex_hull(points)
    if len(hull) < 3:
        return 0.0
    sum1 = 0.0
    sum2 = 0.0
    n = len(hull)
    for i in range(n):
        j = (i + 1) % n
        x1, y1 = hull[i]
        x2, y2 = hull[j]
        sum1 += x1 * y2
        sum2 += y1 * x2
    area = 0.5 * abs(sum1 - sum2)
    return area
if __name__ == '__main__':
    sample_coordinates = [
        (10.0, 20.0),
        (11.0, 21.0),
        (10.5, 20.5),
        (15.0, 25.0),
        (12.0, 23.0)
    ]
    area = calculate_convex_hull_area(sample_coordinates)
    print(area)
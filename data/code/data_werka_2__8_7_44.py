def calculate_convex_hull_area(coordinates):
    n = len(coordinates)
    if n < 3:
        return 0.0
    coordinates.sort()
    lower = []
    for point in coordinates:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(coordinates):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    hull = lower[:-1] + upper[:-1]
    area = 0.0
    for i in range(len(hull)):
        x1, y1 = hull[i]
        x2, y2 = hull[(i + 1) % len(hull)]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2.0

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
if __name__ == '__main__':
    sample_coordinates = [(0, 0), (4, 0), (4, 3), (0, 3)]
    area = calculate_convex_hull_area(sample_coordinates)
    print(area)
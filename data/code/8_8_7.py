import math

def calculate_convex_hull_area(coordinates):
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def get_convex_hull(points):
        if len(points) <= 1:
            return points
        points = sorted(set(points))
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

    def polygon_area(vertices):
        n = len(vertices)
        if n < 3:
            return 0.0
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += vertices[i][0] * vertices[j][1]
            area -= vertices[j][0] * vertices[i][1]
        return abs(area) / 2.0

    hull_vertices = get_convex_hull(coordinates)
    return polygon_area(hull_vertices)

if __name__ == '__main__':
    sample_points = [
        (40.7128, -74.0060),
        (40.7580, -73.9855),
        (40.7061, -74.0087),
        (40.7282, -73.9942),
        (40.7484, -73.9857)
    ]
    result = calculate_convex_hull_area(sample_points)
    print(result)
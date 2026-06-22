import math

class ConvexHullCalculator:
    def __init__(self, coordinates):
        self.coordinates = sorted(coordinates, key=lambda p: (p[0], p[1]))
        if len(self.coordinates) < 3:
            raise ValueError('At least three points are required to form a convex hull.')

    def cross_product(self, o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def compute_hull(self, points):
        hull = []
        for p in points:
            while len(hull) >= 2 and self.cross_product(hull[-2], hull[-1], p) <= 0:
                hull.pop()
            hull.append(p)
        return hull

    def calculate_area(self):
        lower_hull = self.compute_hull(self.coordinates)
        upper_hull = self.compute_hull(reversed(self.coordinates))
        hull = lower_hull[:-1] + upper_hull[:-1]
        area = 0.0
        for i in range(len(hull)):
            j = (i + 1) % len(hull)
            area += hull[i][0] * hull[j][1]
            area -= hull[j][0] * hull[i][1]
        return abs(area) / 2.0

if __name__ == '__main__':
    sample_coordinates = [(0, 0), (4, 0), (4, 3), (0, 3)]
    calculator = ConvexHullCalculator(sample_coordinates)
    print(calculator.calculate_area())
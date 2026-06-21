class ConvexHullCalculator:
    def __init__(self, coordinates):
        if len(coordinates) < 3:
            raise ValueError('At least three points are required to form a convex hull.')
        self.coordinates = sorted(coordinates, key=lambda p: (p[0], p[1]))

    def cross_product(self, o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def compute_hull(self):
        lower = []
        for p in self.coordinates:
            while len(lower) >= 2 and self.cross_product(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(self.coordinates):
            while len(upper) >= 2 and self.cross_product(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)

        return lower[:-1] + upper[:-1]

    def calculate_area(self):
        hull = self.compute_hull()
        n = len(hull)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += hull[i][0] * hull[j][1]
            area -= hull[j][0] * hull[i][1]
        return abs(area) / 2.0

if __name__ == '__main__':
    sample_coordinates = [(0, 0), (4, 0), (4, 3), (0, 3)]
    calculator = ConvexHullCalculator(sample_coordinates)
    print("Convex Hull Area:", calculator.calculate_area())
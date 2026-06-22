import numpy as np

class PolygonAreaCalculator:
    def __init__(self, points):
        self.points = points
        self.area = self.calculate_area()

    def calculate_area(self):
        x = [p[0] for p in self.points]
        y = [p[1] for p in self.points]
        return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

    def compare_to_circle(self, radius):
        circle_area = np.pi * radius ** 2
        comparison = "Polygon area is greater than circle" if self.area > circle_area else \
                     ("Polygon area is less than circle" if self.area < circle_area else "Areas are equal")
        return circle_area, comparison

if __name__ == '__main__':
    polygon_points = [(0, 0), (2, 0), (2, 2), (0, 2)]
    calculator = PolygonAreaCalculator(polygon_points)
    print(f"Polygon area: {calculator.area}")
    circle_radius = 1.5
    circle_area, comparison_result = calculator.compare_to_circle(circle_radius)
    print(f"Circle area with radius {circle_radius}: {circle_area}")
    print(comparison_result)
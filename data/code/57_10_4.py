import math

class GeometryCalculator:

    def circle_area(self, radius):
        return math.pi * radius ** 2

    def triangle_area(self, base, height):
        return 0.5 * base * height
if __name__ == '__main__':
    calculator = GeometryCalculator()
    circle_radius = 6
    print(calculator.circle_area(circle_radius))
    triangle_base = 9
    triangle_height = 4
    print(calculator.triangle_area(triangle_base, triangle_height))
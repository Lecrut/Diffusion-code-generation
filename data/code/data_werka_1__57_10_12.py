import math

class AreaCalculator:

    def calculate_circle(self, radius):
        return math.pi * radius ** 2

    def calculate_triangle(self, base, height):
        return 0.5 * base * height
if __name__ == '__main__':
    calculator = AreaCalculator()
    circle_radius = 3
    print(calculator.calculate_circle(circle_radius))
    triangle_base = 6
    triangle_height = 4
    print(calculator.calculate_triangle(triangle_base, triangle_height))
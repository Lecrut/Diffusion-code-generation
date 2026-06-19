import math

class AreaCalculator:

    def __init__(self):
        self.PI = math.pi

    def calculate_circle_area(self, radius):
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        return self.PI * radius ** 2

    def calculate_triangle_area(self, base, height):
        if base < 0 or height < 0:
            raise ValueError('Base and height cannot be negative')
        return 0.5 * base * height
if __name__ == '__main__':
    calculator = AreaCalculator()
    circle_radius = 5
    print(calculator.calculate_circle_area(circle_radius))
    triangle_base = 10
    triangle_height = 4
    print(calculator.calculate_triangle_area(triangle_base, triangle_height))
import math

class ShapeCalculator:
    def calculate_circle_area(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius ** 2

    def calculate_triangle_area(self, base, height):
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative")
        return 0.5 * base * height

if __name__ == '__main__':
    calculator = ShapeCalculator()
    try:
        shape = 'circle'
        radius = 5
        if shape == 'circle':
            area = calculator.calculate_circle_area(radius)
            print(area)
        elif shape == 'triangle':
            base = 10
            height = 4
            area = calculator.calculate_triangle_area(base, height)
            print(area)
    except ValueError as e:
        print(e)
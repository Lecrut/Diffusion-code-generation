import math

class GeometryCalculator:
    def rectangle_area(self, length, width):
        return length * width

    def circle_area(self, radius):
        return math.pi * radius ** 2

    def triangle_area(self, base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    calculator = GeometryCalculator()
    rectangle_area = calculator.rectangle_area(6, 4)
    circle_area = calculator.circle_area(10)
    triangle_area = calculator.triangle_area(7, 3)

    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")
    print(f"Triangle Area: {triangle_area}")
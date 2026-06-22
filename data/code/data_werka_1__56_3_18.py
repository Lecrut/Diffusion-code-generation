import math

class ShapeAreaCalculator:
    PI = math.pi

    @staticmethod
    def calculate_area_rectangle(length, width):
        return length * width

    @staticmethod
    def calculate_area_circle(radius):
        return ShapeAreaCalculator.PI * radius ** 2

    @staticmethod
    def compare_areas(length, width, radius):
        rectangle_area = ShapeAreaCalculator.calculate_area_rectangle(length, width)
        circle_area = ShapeAreaCalculator.calculate_area_circle(radius)
        print(f"Rectangle Area: {rectangle_area:.2f}")
        print(f"Circle Area: {circle_area:.2f}")

if __name__ == '__main__':
    length = 8.0
    width = 3.5
    radius = 4.5
    ShapeAreaCalculator.compare_areas(length, width, radius)
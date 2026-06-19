import math

class ShapeCalculator:
    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def circle_perimeter(radius):
        return 2 * math.pi * radius

    @staticmethod
    def rectangle_area(length, width):
        return length * width

    @staticmethod
    def rectangle_perimeter(length, width):
        return 2 * (length + width)

if __name__ == '__main__':
    circle_radius = 7
    rectangle_length = 9
    rectangle_width = 3

    circle_area_result = ShapeCalculator.circle_area(circle_radius)
    circle_perimeter_result = ShapeCalculator.circle_perimeter(circle_radius)
    rectangle_area_result = ShapeCalculator.rectangle_area(rectangle_length, rectangle_width)
    rectangle_perimeter_result = ShapeCalculator.rectangle_perimeter(rectangle_length, rectangle_width)

    print(f"Circle with radius {circle_radius}:")
    print(f"  Area: {circle_area_result}")
    print(f"  Perimeter: {circle_perimeter_result}")

    print(f"\nRectangle with length {rectangle_length} and width {rectangle_width}:")
    print(f"  Area: {rectangle_area_result}")
    print(f"  Perimeter: {rectangle_perimeter_result}")
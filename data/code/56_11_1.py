import math
class Shapes:
    def calculate_circle_area(self, radius):
        return math.pi * (radius ** 2)
    def calculate_circle_perimeter(self, radius):
        return 2 * math.pi * radius
    def calculate_square_area(self, side):
        return side ** 2
    def calculate_square_perimeter(self, side):
        return 4 * side
if __name__ == '__main__':
    shapes = Shapes()
    circle_radius = 5.0
    circle_area = shapes.calculate_circle_area(circle_radius)
    circle_perimeter = shapes.calculate_circle_perimeter(circle_radius)
    print(f"Circle Radius: {circle_radius}")
    print(f"Circle Area: {circle_area}")
    print(f"Circle Perimeter (Circumference): {circle_perimeter}")
    print("-" * 20)
    square_side = 4.0
    square_area = shapes.calculate_square_area(square_side)
    square_perimeter = shapes.calculate_square_perimeter(square_side)
    print(f"Square Side: {square_side}")
    print(f"Square Area: {square_area}")
    print(f"Square Perimeter: {square_perimeter}")
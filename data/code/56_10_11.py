import math

class Shapes:
    def __init__(self, radius=0, side_length=0):
        self.radius = radius
        self.side_length = side_length

    @staticmethod
    def circle_area(radius):
        return math.pi * (radius ** 2)

    @staticmethod
    def circle_perimeter(radius):
        return 2 * math.pi * radius

    @staticmethod
    def square_area(side_length):
        return side_length ** 2

    @staticmethod
    def square_perimeter(side_length):
        return 4 * side_length

if __name__ == '__main__':
    circle_radius = 7.0
    square_side_length = 6.0
    print(f"Circle:")
    print(f"Radius: {circle_radius}")
    print(f"Area: {Shapes.circle_area(circle_radius)}")
    print(f"Perimeter (Circumference): {Shapes.circle_perimeter(circle_radius)}")
    print("\nSquare:")
    print(f"Side Length: {square_side_length}")
    print(f"Area: {Shapes.square_area(square_side_length)}")
    print(f"Perimeter: {Shapes.square_perimeter(square_side_length)}")
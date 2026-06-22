import math

class Shapes:
    def __init__(self, circle_radius=0, square_side_length=0):
        self.circle_radius = circle_radius
        self.square_side_length = square_side_length

    def circle_area(self):
        return math.pi * (self.circle_radius ** 2)

    def circle_perimeter(self):
        return 2 * math.pi * self.circle_radius

    def square_area(self):
        return self.square_side_length ** 2

    def square_perimeter(self):
        return 4 * self.square_side_length

if __name__ == '__main__':
    shape = Shapes(circle_radius=5, square_side_length=10)
    
    print("Circle:")
    print(f"Radius: {shape.circle_radius}")
    print(f"Area: {shape.circle_area()}")
    print(f"Perimeter (Circumference): {shape.circle_perimeter()}")
    
    print("\nSquare:")
    print(f"Side Length: {shape.square_side_length}")
    print(f"Area: {shape.square_area()}")
    print(f"Perimeter: {shape.square_perimeter()}")
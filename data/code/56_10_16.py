import math

class Shapes:
    def __init__(self, circle_radius=0.0, square_side_length=0.0):
        self.circle_radius = circle_radius
        self.square_side_length = square_side_length

    def calculate_circle_area(self):
        return math.pi * (self.circle_radius ** 2)

    def calculate_circle_perimeter(self):
        return 2 * math.pi * self.circle_radius

    def calculate_square_area(self):
        return self.square_side_length ** 2

    def calculate_square_perimeter(self):
        return 4 * self.square_side_length

if __name__ == '__main__':
    circle_sample_radius = 7.0
    square_sample_side_length = 8.0

    shape_instance = Shapes(circle_radius=circle_sample_radius, square_side_length=square_sample_side_length)

    print("Circle Area:", shape_instance.calculate_circle_area())
    print("Circle Perimeter:", shape_instance.calculate_circle_perimeter())
    print("Square Area:", shape_instance.calculate_square_area())
    print("Square Perimeter:", shape_instance.calculate_square_perimeter())
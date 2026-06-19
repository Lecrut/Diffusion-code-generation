import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Square:
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Side length must be positive")
        self.side = side

    def perimeter(self):
        return 4 * self.side

def calculate_areas_and_perimeters(circle_radii, square_sides):
    total_circle_area = sum(Circle(radius).area() for radius in circle_radii)
    total_square_perimeter = sum(Square(side).perimeter() for side in square_sides)
    return {
        "total_circle_area": total_circle_area,
        "total_square_perimeter": total_square_perimeter
    }

if __name__ == '__main__':
    circle_radii = [3.0, 5.0]
    square_sides = [4.0, 6.0]
    result = calculate_areas_and_perimeters(circle_radii, square_sides)
    print(result)
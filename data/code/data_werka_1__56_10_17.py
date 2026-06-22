import math

class Shapes:

    def __init__(self, radius=0, side_length=0):
        self.radius = radius
        self.side_length = side_length

    def circle_area(self):
        return math.pi * self.radius ** 2

    def circle_perimeter(self):
        return 2 * math.pi * self.radius

    def square_area(self):
        return self.side_length ** 2

    def square_perimeter(self):
        return 4 * self.side_length
if __name__ == '__main__':
    circle_radius = 7.0
    square_side = 6.0
    shape = Shapes(radius=circle_radius, side_length=square_side)
    circle_area_result = shape.circle_area()
    circle_perimeter_result = shape.circle_perimeter()
    square_area_result = shape.square_area()
    square_perimeter_result = shape.square_perimeter()
    print(f'Circle:')
    print(f'Radius: {circle_radius}')
    print(f'Area: {circle_area_result}')
    print(f'Perimeter (Circumference): {circle_perimeter_result}')
    print('\nSquare:')
    print(f'Side Length: {square_side}')
    print(f'Area: {square_area_result}')
    print(f'Perimeter: {square_perimeter_result}')
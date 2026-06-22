import math

class Shapes:
    def __init__(self, radius=0, side_length=0):
        self.radius = radius
        self.side_length = side_length

    def area(self, shape_type='circle'):
        if shape_type == 'circle':
            return math.pi * (self.radius ** 2)
        elif shape_type == 'square':
            return self.side_length ** 2
        else:
            raise ValueError("Invalid shape type")

    def perimeter(self, shape_type='circle'):
        if shape_type == 'circle':
            return 2 * math.pi * self.radius
        elif shape_type == 'square':
            return 4 * self.side_length
        else:
            raise ValueError("Invalid shape type")

if __name__ == '__main__':
    circle_radius = 5.0
    square_side_length = 10.0

    shapes = Shapes(radius=circle_radius, side_length=square_side_length)
    
    print(f"Circle Area: {shapes.area('circle')}")
    print(f"Circle Perimeter (Circumference): {shapes.perimeter('circle')}")
    print(f"Square Area: {shapes.area('square')}")
    print(f"Square Perimeter: {shapes.perimeter('square')}")
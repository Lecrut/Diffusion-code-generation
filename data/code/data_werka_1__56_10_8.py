import math

class Shapes:
    def __init__(self, radius=0, side_length=0):
        self.radius = radius
        self.side_length = side_length
    
    def area(self, shape_type):
        if shape_type == 'circle':
            return math.pi * (self.radius ** 2)
        elif shape_type == 'square':
            return self.side_length ** 2
        else:
            raise ValueError("Unsupported shape type")
    
    def perimeter(self, shape_type):
        if shape_type == 'circle':
            return 2 * math.pi * self.radius
        elif shape_type == 'square':
            return 4 * self.side_length
        else:
            raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    circle_radius = 5.0
    square_side_length = 10.0
    
    shape = Shapes(radius=circle_radius, side_length=square_side_length)
    
    print(f"Circle Area: {shape.area('circle')}")
    print(f"Circle Perimeter (Circumference): {shape.perimeter('circle')}")
    print(f"Square Area: {shape.area('square')}")
    print(f"Square Perimeter: {shape.perimeter('square')}")
import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

def scaled_area(shape, dimensions, scale_factor):
    if isinstance(shape, Rectangle):
        area = shape.area()
    elif isinstance(shape, Circle):
        area = shape.area()
    else:
        raise ValueError("Unsupported shape")
    return area * scale_factor

if __name__ == '__main__':
    rectangle = Rectangle(5, 10)
    circle = Circle(7)
    scale_factor = 2.5
    rectangle_scaled_area = scaled_area(rectangle, None, scale_factor)
    circle_scaled_area = scaled_area(circle, None, scale_factor)
    print(f'Scaled area of the rectangle: {rectangle_scaled_area}')
    print(f'Scaled area of the circle: {circle_scaled_area}')
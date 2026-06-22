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

def calculate_scaled_area(shape, scale_factor):
    return shape.area() * scale_factor

if __name__ == '__main__':
    rectangle_dimensions = (5, 10)
    circle_dimensions = (7,)
    scale_factor = 2.5
    
    rectangle = Rectangle(*rectangle_dimensions)
    circle = Circle(*circle_dimensions)
    
    rectangle_scaled_area = calculate_scaled_area(rectangle, scale_factor)
    circle_scaled_area = calculate_scaled_area(circle, scale_factor)
    
    print(f'Scaled area of the rectangle: {rectangle_scaled_area}')
    print(f'Scaled area of the circle: {circle_scaled_area}')
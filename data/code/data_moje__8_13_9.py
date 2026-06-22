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
        return math.pi * self.radius ** 2

def scaled_area(shape, scale_factor):
    return shape.area() * scale_factor

def calculate_scaled_areas(rectangle_dims, circle_radius, scale_factor):
    rectangle = Rectangle(*rectangle_dims)
    circle = Circle(circle_radius)
    rect_scaled = scaled_area(rectangle, scale_factor)
    circ_scaled = scaled_area(circle, scale_factor)
    return rect_scaled, circ_scaled

if __name__ == '__main__':
    rectangle_dimensions = (10, 5)
    circle_radius = 7
    scale_factor = 2.5
    rect_area, circ_area = calculate_scaled_areas(
        rectangle_dimensions, circle_radius, scale_factor
    )
    print(rect_area)
    print(circ_area)
import math

def is_valid_radius(radius):
    return radius >= 0

class Circle:
    def __init__(self, radius):
        if not is_valid_radius(radius):
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

def calculate_circle_area(radius):
    if not is_valid_radius(radius):
        raise ValueError("Radius cannot be negative")
    circle = Circle(radius)
    return circle.area()

if __name__ == '__main__':
    try:
        radius = 10.0
        area = calculate_circle_area(radius)
        print(area)
    except ValueError as e:
        print(e)
import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")

class Circle:
    def __init__(self, radius):
        validate_radius(radius)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

def calculate_circle_area(radius):
    validate_radius(radius)
    circle = Circle(radius)
    return circle.area()

if __name__ == '__main__':
    try:
        sample_radius = 10.0
        area_result = calculate_circle_area(sample_radius)
        print(f"The area of the circle with radius {sample_radius} is: {area_result}")
    except (TypeError, ValueError) as e:
        print(e)
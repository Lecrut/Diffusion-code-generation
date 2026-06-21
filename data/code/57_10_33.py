import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius cannot be negative")

def calculate_circle_area(radius):
    validate_radius(radius)
    return math.pi * (radius ** 2)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return calculate_circle_area(self.radius)

if __name__ == '__main__':
    sample_radius = 5
    circle_instance = Circle(sample_radius)
    print(circle_instance.area())
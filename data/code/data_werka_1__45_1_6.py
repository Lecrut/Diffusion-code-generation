import math

def validate_radius(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")

class Circle:
    def __init__(self, radius):
        validate_radius(radius)
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    try:
        sample_radius = 10.0
        circle = Circle(sample_radius)
        print(circle.area())
    except ValueError as e:
        print(e)
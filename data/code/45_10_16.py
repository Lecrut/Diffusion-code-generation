import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return calculate_circle_area(self.radius)

if __name__ == '__main__':
    sample_radius = 3.0
    circle = Circle(sample_radius)
    print(circle.area())
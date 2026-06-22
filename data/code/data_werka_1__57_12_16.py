import math

class Circle:
    def __init__(self, radius):
        if not isinstance(radius, (int, float)) or radius < 0:
            raise ValueError("Radius must be a non-negative number")
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    sample_radius = 5
    circle = Circle(sample_radius)
    area = circle.calculate_area()
    print(area)
import math

class Circle:
    def __init__(self, radius):
        self.radius = self.validate_radius(radius)
    
    def validate_radius(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number.")
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        return radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    circle = Circle(5.0)
    area = circle.calculate_area()
    print(f"Area of circle with radius 5.0: {area}")
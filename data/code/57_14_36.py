import math

class Circle:
    PI = math.pi
    
    def __init__(self, radius):
        self.radius = self.validate_radius(radius)
    
    @staticmethod
    def validate_radius(radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return radius
    
    def area(self):
        return Circle.PI * self.radius ** 2

if __name__ == '__main__':
    sample_radius = 4.0
    circle = Circle(sample_radius)
    print(circle.area())
import math

class Circle:
    PI = math.pi
    
    def __init__(self, radius):
        self.radius = radius
    
    @staticmethod
    def validate_radius(radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
        if radius < 0:
            raise ValueError("Radius cannot be negative")
    
    def area(self):
        Circle.validate_radius(self.radius)
        return Circle.PI * self.radius ** 2

if __name__ == '__main__':
    sample_radius = 6.5
    circle = Circle(sample_radius)
    print(circle.area())
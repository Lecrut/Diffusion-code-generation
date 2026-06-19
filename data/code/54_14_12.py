import math

class Circle:
    def __init__(self, radius):
        self.radius = self.validate_radius(radius)
    
    @staticmethod
    def validate_radius(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    try:
        sample_radius = 10.0
        circle = Circle(sample_radius)
        print(circle.area())
    except ValueError as e:
        print(e)
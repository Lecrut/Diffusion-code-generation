import math

class Circle:
    PI = math.pi
    
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    @staticmethod
    def calculate_perimeter(radius):
        return 2 * Circle.PI * radius

if __name__ == '__main__':
    sample_radius = 8
    try:
        circle = Circle(sample_radius)
        perimeter = Circle.calculate_perimeter(circle.radius)
        print(perimeter)
    except ValueError as e:
        print(e)
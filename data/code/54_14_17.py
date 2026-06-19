import math

class Circle:
    PI = math.pi
    
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    @staticmethod
    def calculate_area(radius):
        return Circle.PI * radius ** 2
    
    def area(self):
        return Circle.calculate_area(self.radius)

if __name__ == '__main__':
    sample_radius = 6.0
    try:
        circle = Circle(sample_radius)
        print("Area of the circle:", circle.area())
    except ValueError as e:
        print(e)
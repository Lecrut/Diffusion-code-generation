import math

class Circle:
    DEFAULT_RADIUS = 5
    
    def __init__(self, radius=DEFAULT_RADIUS):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    @staticmethod
    def calculate_area(radius):
        return math.pi * radius ** 2
    
    def area(self):
        return Circle.calculate_area(self.radius)

if __name__ == '__main__':
    circle = Circle()
    print(circle.area())
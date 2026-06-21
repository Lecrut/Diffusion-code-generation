import math

class Circle:
    DEFAULT_RADIUS = 5
    
    @staticmethod
    def calculate_area(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius ** 2
    
    def __init__(self, radius=DEFAULT_RADIUS):
        self.radius = radius
    
    def area(self):
        return Circle.calculate_area(self.radius)

if __name__ == '__main__':
    circle = Circle()
    print(circle.area())
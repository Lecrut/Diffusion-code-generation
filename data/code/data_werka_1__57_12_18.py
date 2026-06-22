import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def get_radius(self):
        return self.radius

if __name__ == '__main__':
    circle = Circle(5)
    area = circle.calculate_area()
    radius = circle.get_radius()
    
    print(f"Area of the circle: {area}")
    print(f"Radius of the circle: {radius}")
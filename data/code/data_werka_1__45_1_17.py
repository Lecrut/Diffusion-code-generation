import math

class Circle:
    PI = math.pi
    
    def __init__(self, radius):
        self.radius = radius
    
    @staticmethod
    def calculate_area(radius):
        return Circle.PI * (radius ** 2)
    
    def area(self):
        return Circle.calculate_area(self.radius)

if __name__ == '__main__':
    sample_radius = 5.0
    circle = Circle(sample_radius)
    print(circle.area())
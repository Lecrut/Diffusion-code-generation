import math

class Circle:
    PI = math.pi
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.PI * (self.radius ** 2)

if __name__ == '__main__':
    sample_radius = 3.0
    circle = Circle(sample_radius)
    print(circle.area())
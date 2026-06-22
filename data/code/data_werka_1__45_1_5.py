import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def diameter(self):
        return 2 * self.radius

if __name__ == '__main__':
    sample_radius = 10.0
    circle_instance = Circle(sample_radius)
    print(circle_instance.area())
    print(circle_instance.diameter())
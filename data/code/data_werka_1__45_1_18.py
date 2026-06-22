import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    SAMPLE_RADIUS = 10.0
    circle = Circle(SAMPLE_RADIUS)
    print(circle.area())
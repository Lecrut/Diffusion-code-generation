import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_circumference(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    circle = Circle(2.5)
    circumference = circle.calculate_circumference()
    print(circumference)
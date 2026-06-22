import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    circle1 = Circle(3.0)
    area1 = circle1.calculate_area()
    print(f"Area of circle 1 with radius {circle1.radius}: {area1:.2f}")
    
    circle2 = Circle(7.5)
    area2 = circle2.calculate_area()
    print(f"Area of circle 2 with radius {circle2.radius}: {area2:.2f}")
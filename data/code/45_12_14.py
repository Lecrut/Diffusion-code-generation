import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    circle_radius_1 = 7.0
    circle1 = Circle(circle_radius_1)
    area1 = circle1.calculate_area()
    print(f"Area of circle with radius {circle_radius_1}: {area1}")

    circle_radius_2 = 3.5
    circle2 = Circle(circle_radius_2)
    area2 = circle2.calculate_area()
    print(f"Area of circle with radius {circle_radius_2}: {area2}")
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

def calculate_circle_area(radius):
    circle = Circle(radius)
    return circle.area()

if __name__ == '__main__':
    sample_radius1 = 4.0
    sample_radius2 = 9.5
    area1 = calculate_circle_area(sample_radius1)
    area2 = calculate_circle_area(sample_radius2)
    print(area1)
    print(area2)
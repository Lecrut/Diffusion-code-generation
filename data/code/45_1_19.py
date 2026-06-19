import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    test_radius = 3.5
    circle_instance = Circle(test_radius)
    area_of_circle = circle_instance.calculate_area()
    print(area_of_circle)
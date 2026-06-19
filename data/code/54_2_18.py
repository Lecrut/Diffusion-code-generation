import math

class Circle:
    PI = math.pi
    
    def __init__(self, radius):
        self.radius = radius
    
    @staticmethod
    def area(radius):
        return Circle.PI * radius ** 2

if __name__ == '__main__':
    sample_radius = 4.5
    circle_area = Circle.area(sample_radius)
    print(circle_area)
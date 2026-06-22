import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    circle_instance = Circle(5)
    print(circle_instance.calculate_perimeter())
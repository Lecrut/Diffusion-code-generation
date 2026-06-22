import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    circle_config = {'radius': 6}
    circle_instance = Circle(circle_config['radius'])
    print(circle_instance.perimeter())
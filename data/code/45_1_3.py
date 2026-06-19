import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_values = {'radius': 7.0}
    circle_instance = Circle(sample_values['radius'])
    print(circle_instance.area())
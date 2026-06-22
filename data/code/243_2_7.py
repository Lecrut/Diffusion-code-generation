import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_perimeter(self):
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    sample_circle = Circle(5.0)
    print(sample_circle.get_perimeter())
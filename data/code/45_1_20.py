import math
PI = math.pi

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2
if __name__ == '__main__':
    sample_radius = 3.0
    circle_instance = Circle(sample_radius)
    print(circle_instance.area())
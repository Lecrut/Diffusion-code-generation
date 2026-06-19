import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    SAMPLE_RADIUS = 7.5
    circle_instance = Circle(SAMPLE_RADIUS)
    area = circle_instance.calculate_area()
    print(area)
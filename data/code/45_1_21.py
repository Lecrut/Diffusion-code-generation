import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_radius_value = 3.5
    circle_object = Circle(sample_radius_value)
    calculated_area = circle_object.area()
    print(calculated_area)
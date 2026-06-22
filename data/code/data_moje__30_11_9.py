import math

PI_CONST = math.pi
RADIUS_VALUE = 5

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return PI_CONST * self.radius ** 2

if __name__ == '__main__':
    instance = Circle(RADIUS_VALUE)
    calculated_area = instance.get_area()
    print(calculated_area)
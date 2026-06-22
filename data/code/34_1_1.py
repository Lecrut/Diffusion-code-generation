import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        base_area = math.pi * self.radius ** 2
        lateral_area = 2 * math.pi * self.radius * self.height
        return 2 * base_area + lateral_area

if __name__ == '__main__':
    cylinder = Cylinder(radius=5, height=10)
    print(cylinder.surface_area())
import math

class ConeGeometry:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.pi = math.pi

    def calculate_base_area(self):
        return self.pi * self.radius * self.radius

    def calculate_volume(self):
        base_area = self.calculate_base_area()
        return base_area * self.height / 3

    def get_dimensions(self):
        return self.radius, self.height

if __name__ == '__main__':
    cone = ConeGeometry(radius=3, height=7)
    vol = cone.calculate_volume()
    base_area = cone.calculate_base_area()
    dims = cone.get_dimensions()
    print(vol)
    print(base_area)
    print(dims)
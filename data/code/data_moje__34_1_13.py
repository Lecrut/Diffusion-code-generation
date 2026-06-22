import math

class Cylinder:
    def __init__(self, radius, height):
        self._radius = radius
        self._height = height

    def surface_area(self):
        radius = self._radius
        height = self._height
        pi = math.pi
        
        top_bottom_area = 2 * pi * radius ** 2
        lateral_area = 2 * pi * radius * height
        
        total = top_bottom_area + lateral_area
        return total

if __name__ == '__main__':
    base = Cylinder(radius=4, height=7)
    area_value = base.surface_area()
    print(area_value)
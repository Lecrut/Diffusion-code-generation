import math

class CylinderGeometry:
    _pi = math.pi

    @staticmethod
    def _base_area(radius):
        return CylinderGeometry._pi * (radius ** 2)

    @staticmethod
    def _lateral_area(radius, height):
        return 2 * CylinderGeometry._pi * radius * height

    @staticmethod
    def total_surface_area(radius, height):
        return 2 * CylinderGeometry._base_area(radius) + CylinderGeometry._lateral_area(radius, height)

if __name__ == '__main__':
    radius_value = 3.0
    height_value = 7.0
    surface = CylinderGeometry.total_surface_area(radius_value, height_value)
    print(surface)
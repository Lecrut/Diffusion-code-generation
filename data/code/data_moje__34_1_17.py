import math

PI = math.pi
TWO = 2.0
BASE_SURFACE_FACTOR = TWO
LATERAL_FACTOR = TWO

class Cylinder:
    def __init__(self, radius: float, height: float):
        if radius < 0 or height < 0:
            raise ValueError("Dimensions must be non-negative")
        self.radius = radius
        self.height = height

    def surface_area(self) -> float:
        circle_area = PI * (self.radius ** 2)
        base_surface = BASE_SURFACE_FACTOR * circle_area
        lateral_surface = LATERAL_FACTOR * PI * self.radius * self.height
        return base_surface + lateral_surface

if __name__ == '__main__':
    cylinder_obj = Cylinder(radius=7.5, height=12.0)
    area_result = cylinder_obj.surface_area()
    print(area_result)
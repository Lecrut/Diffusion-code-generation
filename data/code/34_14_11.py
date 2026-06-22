import math

class Cylinder:
    def __init__(self, radius: float, height: float) -> None:
        if radius <= 0:
            raise ValueError("Radius must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")
        self._radius = radius
        self._height = height

    def get_total_surface_area(self) -> float:
        base_area = math.pi * self._radius ** 2
        lateral_area = 2 * math.pi * self._radius * self._height
        return 2 * base_area + lateral_area

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def height(self) -> float:
        return self._height

if __name__ == '__main__':
    SAMPLE_RADIUS = 7.5
    SAMPLE_HEIGHT = 12.0
    cylinder_instance = Cylinder(SAMPLE_RADIUS, SAMPLE_HEIGHT)
    area_value = cylinder_instance.get_total_surface_area()
    print(area_value)
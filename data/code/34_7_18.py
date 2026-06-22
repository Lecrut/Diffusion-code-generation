import math

class CylinderCalculator:
    def __init__(self, radius: float, height: float) -> None:
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        if height <= 0:
            raise ValueError("Height must be a positive number.")
        self._radius = radius
        self._height = height

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def height(self) -> float:
        return self._height

    def calculate_total_surface_area(self) -> float:
        lateral_area = 2 * math.pi * self._radius * self._height
        base_area = 2 * math.pi * self._radius ** 2
        return lateral_area + base_area

    @staticmethod
    def compute_area(radius: float, height: float) -> float:
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        if height <= 0:
            raise ValueError("Height must be positive.")
        return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    sample_radius = 3.5
    sample_height = 7.2
    try:
        calculator = CylinderCalculator(sample_radius, sample_height)
        result_via_instance = calculator.calculate_total_surface_area()
        print(result_via_instance)
    except ValueError as e:
        print(f"Error: {e}")
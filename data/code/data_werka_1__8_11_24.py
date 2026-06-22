from typing import Union

class GeometricShape:

    def __init__(self, area: float):
        self.area = area

    def scale_area(self, factor: float) -> None:
        self.area *= factor

    def get_scaled_area(self, factor: float) -> float:
        return self.area * factor
if __name__ == '__main__':
    circle_area = 28.27
    rectangle_area = 45.0
    scale_factor = 1.5
    circle = GeometricShape(circle_area)
    rectangle = GeometricShape(rectangle_area)
    circle.scale_area(scale_factor)
    rectangle.scale_area(scale_factor)
    print(f'Scaled Circle Area: {circle.get_scaled_area(1.0)}')
    print(f'Scaled Rectangle Area: {rectangle.get_scaled_area(1.0)}')
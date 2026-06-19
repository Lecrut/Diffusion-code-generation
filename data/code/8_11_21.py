from typing import Union

class GeometricShape:

    def __init__(self, area: float):
        self.area = area

    def calculate_area(self) -> float:
        return self.area

    def scale_area(self, factor: float) -> None:
        self.area *= factor
if __name__ == '__main__':
    circle_area = 3.14
    rectangle_area = 20.0
    triangle_area = 15.0
    circle = GeometricShape(circle_area)
    rectangle = GeometricShape(rectangle_area)
    triangle = GeometricShape(triangle_area)
    scale_factor = 2.0
    circle.scale_area(scale_factor)
    rectangle.scale_area(scale_factor)
    triangle.scale_area(scale_factor)
    print(f'Scaled Circle Area: {circle.calculate_area()}')
    print(f'Scaled Rectangle Area: {rectangle.calculate_area()}')
    print(f'Scaled Triangle Area: {triangle.calculate_area()}')
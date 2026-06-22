from typing import Union

class GeometricShape:

    def __init__(self, area: float):
        self.area = area

    def scale_area(self, factor: float) -> None:
        self.area *= factor

    def get_area(self) -> float:
        return self.area
if __name__ == '__main__':
    circle_area = 3.14
    rectangle_area = 20.0
    scale_factor = 2.5
    circle = GeometricShape(circle_area)
    rectangle = GeometricShape(rectangle_area)
    circle.scale_area(scale_factor)
    rectangle.scale_area(scale_factor)
    print(f'Scaled Circle Area: {circle.get_area()}')
    print(f'Scaled Rectangle Area: {rectangle.get_area()}')
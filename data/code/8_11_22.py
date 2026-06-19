from typing import Union

class GeometricShape:

    def __init__(self, area: float):
        self.area = area

    def scale_area(self, factor: float) -> None:
        self.area *= factor

    def get_scaled_area(self, factor: float) -> float:
        return self.area * factor
if __name__ == '__main__':
    circle = GeometricShape(area=10.0)
    rectangle = GeometricShape(area=20.0)
    print('Original Circle Area:', circle.area)
    circle.scale_area(2)
    print('Scaled Circle Area:', circle.area)
    print('Original Rectangle Area:', rectangle.area)
    scaled_rectangle_area = rectangle.get_scaled_area(1.5)
    print('Scaled Rectangle Area (without modifying original):', scaled_rectangle_area)
from typing import Union

class GeometricShape:

    def __init__(self, area: float):
        self.area = area

    def scale_area(self, factor: float) -> None:
        self.area *= factor

    def get_scaled_area(self, factor: float) -> float:
        return self.area * factor
if __name__ == '__main__':
    circle = GeometricShape(10.0)
    square = GeometricShape(25.0)
    print('Original Circle Area:', circle.area)
    print('Scaled Circle Area (x2):', circle.get_scaled_area(2))
    circle.scale_area(2)
    print('Circle Area after Scaling:', circle.area)
    print('Original Square Area:', square.area)
    print('Scaled Square Area (x1.5):', square.get_scaled_area(1.5))
    square.scale_area(1.5)
    print('Square Area after Scaling:', square.area)
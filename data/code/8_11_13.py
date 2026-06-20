from math import pi

class GeometricShape:
    def __init__(self, area: float) -> None:
        self._area = area

    @property
    def area(self) -> float:
        return self._area

    def scale_area(self, factor: float) -> float:
        self._area *= factor
        return self._area

class Circle(GeometricShape):
    def __init__(self, radius: float) -> None:
        super().__init__(pi * radius ** 2)
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius

class Rectangle(GeometricShape):
    def __init__(self, width: float, height: float) -> None:
        super().__init__(width * height)
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        return self._width

    @property
    def height(self) -> float:
        return self._height

if __name__ == '__main__':
    circle = Circle(radius=5.0)
    scaled_circle_area = circle.scale_area(factor=2.0)
    print(scaled_circle_area)

    rectangle = Rectangle(width=4.0, height=6.0)
    scaled_rectangle_area = rectangle.scale_area(factor=1.5)
    print(scaled_rectangle_area)
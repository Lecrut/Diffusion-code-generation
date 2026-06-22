from typing import Tuple

class RectangularBox:
    def __init__(self, length: float, width: float, height: float) -> None:
        if length <= 0:
            raise ValueError("Length must be positive")
        if width <= 0:
            raise ValueError("Width must be positive")
        if height <= 0:
            raise ValueError("Height must be positive")
        self._length = length
        self._width = width
        self._height = height

    def get_dimensions(self) -> Tuple[float, float, float]:
        return (self._length, self._width, self._height)

    def calculate_surface_area(self) -> float:
        l, w, h = self.get_dimensions()
        return 2 * (l * w + w * h + h * l)

if __name__ == '__main__':
    box_instance = RectangularBox(15.5, 8.2, 3.0)
    area_result = box_instance.calculate_surface_area()
    print(area_result)
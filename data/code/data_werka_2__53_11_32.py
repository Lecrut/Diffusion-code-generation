from typing import Final

class Shape:

    def __init__(self, side_length: float):
        if side_length < 0:
            raise ValueError('Side length cannot be negative')
        self._side_length = side_length

    @property
    def side_length(self) -> float:
        return self._side_length

    @side_length.setter
    def side_length(self, value: float) -> None:
        if value < 0:
            raise ValueError('Side length cannot be negative')
        self._side_length = value

    def calculate_area(self) -> float:
        return self._side_length ** 2
if __name__ == '__main__':
    DEFAULT_SIDE_LENGTH: Final[float] = 5.0
    shape_instance = Shape(DEFAULT_SIDE_LENGTH)
    area = shape_instance.calculate_area()
    print(f'Area of the square with side length {shape_instance.side_length}: {area}')
    try:
        shape_instance.side_length = -3.0
    except ValueError as e:
        print(e)
from typing import Final

class Geometry:
    def __init__(self, side_length: float):
        self.side_length = side_length

    def calculate_area(self) -> float:
        if self.side_length < 0:
            raise ValueError("Side length cannot be negative")
        return self.side_length ** 2

if __name__ == '__main__':
    DEFAULT_SIDE_LENGTH: Final[float] = 5.0
    geometry_instance = Geometry(DEFAULT_SIDE_LENGTH)
    area = geometry_instance.calculate_area()
    print(area)
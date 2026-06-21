from typing import Final

class Shape:
    def __init__(self, side_length: float):
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        self.side_length = side_length

    def calculate_area(self) -> float:
        return self.side_length ** 2

    def describe(self) -> str:
        return f"Shape with side length {self.side_length}"

if __name__ == '__main__':
    DEFAULT_SIDE_LENGTH: Final[float] = 5.0
    shape_instance = Shape(DEFAULT_SIDE_LENGTH)
    area = shape_instance.calculate_area()
    description = shape_instance.describe()
    print(area)
    print(description)
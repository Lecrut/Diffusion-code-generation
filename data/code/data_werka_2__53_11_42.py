from typing import Final

class Square:
    def __init__(self, side_length: float):
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        self.side_length = side_length

    def calculate_area(self) -> float:
        return self.side_length ** 2

if __name__ == '__main__':
    DEFAULT_SIDE_LENGTH: Final[float] = 5.0
    square_instance = Square(DEFAULT_SIDE_LENGTH)
    area = square_instance.calculate_area()
    print(area)
from typing import Final

class Square:
    DEFAULT_SIDE_LENGTH: Final[float] = 5.0

    def __init__(self, side_length: float):
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        self.side_length = side_length

    @staticmethod
    def calculate_area(side_length: float) -> float:
        return side_length ** 2

if __name__ == '__main__':
    square_instance = Square(Square.DEFAULT_SIDE_LENGTH)
    area = square_instance.calculate_area(square_instance.side_length)
    print(area)
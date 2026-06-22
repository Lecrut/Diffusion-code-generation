from typing import Final

class Square:
    DEFAULT_SIDE_LENGTH: Final[float] = 5.0

    def __init__(self, side_length: float = DEFAULT_SIDE_LENGTH):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    @staticmethod
    def calculate_area(side_length: float) -> float:
        return side_length ** 2

if __name__ == '__main__':
    try:
        square = Square()
        area = Square.calculate_area(square.side_length)
        print(area)
    except ValueError as e:
        print(e)
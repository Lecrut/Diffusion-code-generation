from typing import Union

class Square:
    def __init__(self, side_length: Union[int, float]):
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length must be an integer or a float")
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def get_area(self) -> Union[int, float]:
        return self.side_length * self.side_length

if __name__ == '__main__':
    SMALL_SQUARE_SIDE = 3
    MEDIUM_SQUARE_SIDE = 7
    LARGE_SQUARE_SIDE = 10

    squares = [
        Square(SMALL_SQUARE_SIDE),
        Square(MEDIUM_SQUARE_SIDE),
        Square(LARGE_SQUARE_SIDE)
    ]

    for square in squares:
        print(f"The area of a square with side length {square.side_length} is {square.get_area()}")
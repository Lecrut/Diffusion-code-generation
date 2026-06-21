from typing import TypeVar

T = TypeVar('T', int, float)

class Square:
    def __init__(self, side_length: T):
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length must be an integer or a float")
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def get_area(self) -> T:
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_squares = [
        Square(3),
        Square(5.5),
        Square(10)
    ]

    for square in sample_squares:
        print(f"The area of a square with side length {square.side_length} is {square.get_area()}")
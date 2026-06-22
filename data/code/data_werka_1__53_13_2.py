from typing import Any

class Square:
    def __init__(self, side_length: float):
        self.side_length = side_length

    def calculate_area(self) -> float:
        return self.side_length ** 2

if __name__ == '__main__':
    side_length = 5.0
    square = Square(side_length)
    area = square.calculate_area()
    print(area)
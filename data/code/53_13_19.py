from typing import Final

class Square:
    def __init__(self, side_length: float):
        self.side_length = side_length

    def calculate_area(self) -> float:
        return self.side_length ** 2

def main():
    side_length: Final[float] = 5.0
    square = Square(side_length)
    area = square.calculate_area()
    print(area)

if __name__ == '__main__':
    main()
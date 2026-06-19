from typing import Final

class Square:
    def __init__(self, side_length: float):
        self.side_length = side_length

    def calculate_area(self) -> float:
        return self.side_length ** 2

def main():
    try:
        SIDE_LENGTH: Final[float] = 5.0
        square = Square(SIDE_LENGTH)
        area = square.calculate_area()
        print(area)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
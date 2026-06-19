from typing import Dict

class Square:
    def __init__(self, side_length: float):
        self.side_length = side_length
        if not self.is_valid():
            raise ValueError("Side length must be positive")

    def is_valid(self) -> bool:
        return self.side_length > 0

    def calculate_area(self) -> float:
        return self.side_length ** 2

def main():
    try:
        side_length = 5.0
        square = Square(side_length)
        area = square.calculate_area()
        print(area)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
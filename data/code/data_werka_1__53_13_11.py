from typing import Union

class Square:
    def __init__(self, side_length: float):
        self._validate_side_length(side_length)
        self.side_length = side_length

    @staticmethod
    def _validate_side_length(side_length: float) -> None:
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length must be a number")
        if side_length <= 0:
            raise ValueError("Side length must be positive")

    def calculate_area(self) -> float:
        return self.side_length ** 2

def main():
    try:
        side_length = 5.0
        square = Square(side_length)
        area = square.calculate_area()
        print(f"Area: {area}")
    except (TypeError, ValueError) as e:
        print(e)

if __name__ == '__main__':
    main()
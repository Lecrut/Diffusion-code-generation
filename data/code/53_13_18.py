from typing import Union

class Square:
    def __init__(self, side_length: float):
        self.side_length = side_length

    def calculate_area(self) -> float:
        return self._compute_area()

    def _compute_area(self) -> float:
        return self.side_length ** 2

if __name__ == '__main__':
    sample_side_length = 7.0
    square_instance = Square(sample_side_length)
    computed_area = square_instance.calculate_area()
    print(computed_area)
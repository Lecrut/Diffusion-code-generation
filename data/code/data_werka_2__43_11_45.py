from typing import Union

class Square:
    def __init__(self, side_length: Union[int, float]):
        self._validate_side_length(side_length)
        self.side_length = side_length

    def _validate_side_length(self, side_length: Union[int, float]) -> None:
        if not isinstance(side_length, (int, float)):
            raise TypeError('Side length must be an integer or a float')
        if side_length <= 0:
            raise ValueError('Side length must be positive')

    def get_area(self) -> Union[int, float]:
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_values = [2.5, 6, 8]
    for value in sample_values:
        square = Square(value)
        print(f"The area of a square with side length {value} is {square.get_area()}")
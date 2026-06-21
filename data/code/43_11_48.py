from typing import Union

class Square:
    MIN_SIDE_LENGTH = 0.01

    def __init__(self, side_length: Union[int, float]):
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length must be an integer or a float")
        if side_length < self.MIN_SIDE_LENGTH:
            raise ValueError(f"Side length must be at least {self.MIN_SIDE_LENGTH}")
        self.side_length = side_length

    def get_area(self) -> Union[int, float]:
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_values = [2, 5.5, 10]
    for value in sample_values:
        square = Square(value)
        print(f"The area of a square with side length {value} is {square.get_area()}")
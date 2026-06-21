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
    sample_side_lengths = [2, 6.75, 12]
    for idx, length in enumerate(sample_side_lengths):
        square = Square(length)
        area = square.get_area()
        print(f"The area of the {idx + 1}st square with side length {length} is {area}")
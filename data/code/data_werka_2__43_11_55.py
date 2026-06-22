from typing import Union

class Square:

    def __init__(self, side_length: Union[int, float]):
        self.validate_side_length(side_length)
        self.side_length = side_length

    def validate_side_length(self, side_length: Union[int, float]) -> None:
        if not isinstance(side_length, (int, float)):
            raise TypeError('Side length must be an integer or a float')
        if side_length <= 0:
            raise ValueError('Side length must be positive')

    def get_area(self) -> Union[int, float]:
        return self.side_length * self.side_length
if __name__ == '__main__':
    try:
        square1 = Square(5)
        print(f'The area of the square with side length 5 is {square1.get_area()}')
        square2 = Square(8.2)
        print(f'The area of the square with side length 8.2 is {square2.get_area()}')
        invalid_square = Square(-3)
    except (TypeError, ValueError) as e:
        print(e)
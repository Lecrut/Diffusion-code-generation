from typing import Union

class Square:

    def __init__(self, side_length: Union[int, float]):
        if not isinstance(side_length, (int, float)):
            raise TypeError('Side length must be an integer or a float')
        if side_length <= 0:
            raise ValueError('Side length must be positive')
        self.side_length = side_length

    def get_area(self) -> Union[int, float]:
        return self.side_length * self.side_length
if __name__ == '__main__':
    try:
        square1 = Square(4)
        print(f'The area of the square with side length 4 is {square1.get_area()}')
        square2 = Square(7.5)
        print(f'The area of the square with side length 7.5 is {square2.get_area()}')
        invalid_square = Square(-3)
    except (TypeError, ValueError) as e:
        print(e)
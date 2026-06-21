from typing import Union

class Square:

    def __init__(self, side_length: Union[int, float]):
        if not isinstance(side_length, (int, float)):
            raise TypeError('Side length must be an integer or a float')
        if side_length <= 0:
            raise ValueError('Side length must be positive')
        self.side_length = side_length

    def get_area(self) -> Union[int, float]:
        return self.side_length ** 2
if __name__ == '__main__':
    try:
        square1 = Square(5)
        print(f'The area of the first square with side length {square1.side_length} is {square1.get_area()}')
        square2 = Square(8.2)
        print(f'The area of the second square with side length {square2.side_length} is {square2.get_area()}')
        invalid_square = Square(-3)
    except (TypeError, ValueError) as e:
        print(e)
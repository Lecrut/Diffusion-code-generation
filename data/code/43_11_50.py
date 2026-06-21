from typing import Union

class Square:
    def __init__(self, side_length: Union[int, float]):
        if not isinstance(side_length, (int, float)):
            raise TypeError("Side length must be an integer or a float")
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def get_area(self) -> Union[int, float]:
        area = self.side_length * self.side_length
        return area

if __name__ == '__main__':
    try:
        small_square_side = 3
        medium_square_side = 7.5
        large_square_side = 12

        small_square = Square(small_square_side)
        medium_square = Square(medium_square_side)
        large_square = Square(large_square_side)

        print(f"The area of a square with side length {small_square_side} is {small_square.get_area()}")
        print(f"The area of a square with side length {medium_square_side} is {medium_square.get_area()}")
        print(f"The area of a square with side length {large_square_side} is {large_square.get_area()}")

    except (TypeError, ValueError) as e:
        print(e)
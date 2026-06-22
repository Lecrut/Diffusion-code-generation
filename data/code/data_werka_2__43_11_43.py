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
    try:
        small_square = Square(3)
        medium_square = Square(7.5)
        large_square = Square(10)

        print(f"The area of the small square with side length 3 is {small_square.get_area()}")
        print(f"The area of the medium square with side length 7.5 is {medium_square.get_area()}")
        print(f"The area of the large square with side length 10 is {large_square.get_area()}")

    except (TypeError, ValueError) as e:
        print(e)
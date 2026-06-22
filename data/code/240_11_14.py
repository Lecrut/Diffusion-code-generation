from typing import Union

class Square:
    def __init__(self, side_length: Union[int, float]):
        self.side_length = side_length

    def area(self) -> Union[int, float]:
        return self.side_length ** 2

if __name__ == '__main__':
    square = Square(5)
    print(square.area())
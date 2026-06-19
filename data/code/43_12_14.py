from typing import Union

class Square:
    def __init__(self, side_length: Union[int, float]):
        self.side_length = side_length

    def get_area(self) -> Union[int, float]:
        return self.side_length * self.side_length

if __name__ == '__main__':
    square = Square(5)
    print(square.get_area())
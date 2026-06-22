from typing import Union

class Square:
    def __init__(self, side_length: Union[int, float]):
        self.side_length = side_length

    def get_area(self) -> Union[int, float]:
        return self.side_length * self.side_length

if __name__ == '__main__':
    square1 = Square(7)
    area1 = square1.get_area()
    print(f"Area of square 1: {area1}")

    square2 = Square(3.5)
    area2 = square2.get_area()
    print(f"Area of square 2: {area2}")
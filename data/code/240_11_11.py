from typing import Union

class Square:
    def __init__(self, side_length: Union[int, float]) -> None:
        self.side_length = side_length
    
    def area(self) -> Union[int, float]:
        return self.side_length ** 2

if __name__ == '__main__':
    square1 = Square(5)
    print(f"Side: {square1.side_length}, Area: {square1.area()}")
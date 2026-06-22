from typing import Union

class Square:
    def __init__(self, side_length: Union[int, float]) -> None:
        if not isinstance(side_length, (int, float)) or side_length <= 0:
            raise ValueError("Side length must be a positive number")
        self.side_length = side_length
    
    def area(self) -> Union[int, float]:
        return self.side_length ** 2

if __name__ == '__main__':
    square = Square(5)
    print(f"Side: {square.side_length}, Area: {square.area()}")
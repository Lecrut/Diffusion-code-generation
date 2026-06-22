from typing import Union

class Square:
    def __init__(self, side_length: Union[int, float]) -> None:
        self._side_length = side_length
    
    @property
    def side_length(self) -> Union[int, float]:
        return self._side_length
    
    @side_length.setter
    def side_length(self, value: Union[int, float]) -> None:
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Side length must be a positive number")
        self._side_length = value
    
    def area(self) -> Union[int, float]:
        return self._side_length ** 2

if __name__ == '__main__':
    square = Square(5)
    print(f"Side: {square.side_length}, Area: {square.area()}")
    square.side_length = 12.5
    print(f"New Side: {square.side_length}, New Area: {square.area()}")
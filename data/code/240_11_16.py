from typing import Union

class Square:
    def __init__(self, side_length: Union[int, float]) -> None:
        self.side_length = side_length
    
    @staticmethod
    def calculate_area(side_length: Union[int, float]) -> Union[int, float]:
        return side_length ** 2

if __name__ == '__main__':
    square = Square(5)
    print(f"Side: {square.side_length}, Area: {Square.calculate_area(square.side_length)}")
    another_square = Square(12.5)
    print(f"Side: {another_square.side_length}, Area: {Square.calculate_area(another_square.side_length)}")
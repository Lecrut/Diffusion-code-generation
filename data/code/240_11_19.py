from typing import Union

class Square:
    def __init__(self, side_length: Union[int, float]) -> None:
        if not isinstance(side_length, (int, float)) or side_length <= 0:
            raise ValueError("Side length must be a positive number")
        self.side_length = side_length
    
    @staticmethod
    def calculate_area(side_length: Union[int, float]) -> Union[int, float]:
        return side_length ** 2

if __name__ == '__main__':
    square = Square(5)
    print(f"Side: {square.side_length}, Area: {Square.calculate_area(square.side_length)}")
    square2 = Square(12.5)
    print(f"Side: {square2.side_length}, Area: {Square.calculate_area(square2.side_length)}")
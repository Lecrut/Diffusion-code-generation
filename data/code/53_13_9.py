from typing import Union

def validate_side_length(side_length: float) -> None:
    if side_length <= 0:
        raise ValueError("Side length must be positive")

def calculate_area(side_length: float) -> float:
    return side_length ** 2

class Square:
    def __init__(self, side_length: float):
        validate_side_length(side_length)
        self.side_length = side_length
    
    def get_area(self) -> float:
        return calculate_area(self.side_length)

if __name__ == '__main__':
    try:
        side_length = 5.0
        square = Square(side_length)
        area = square.get_area()
        print(area)
    except ValueError as e:
        print(e)
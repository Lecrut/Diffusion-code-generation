from typing import Any

class Square:
    DEFAULT_SIDE_LENGTH = 5.0
    
    def __init__(self, side_length: float = DEFAULT_SIDE_LENGTH):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length
    
    @staticmethod
    def calculate_area(side_length: float) -> float:
        return side_length ** 2
    
    def get_area(self) -> float:
        return Square.calculate_area(self.side_length)

if __name__ == '__main__':
    try:
        square = Square()
        area = square.get_area()
        print(area)
    except ValueError as e:
        print(e)
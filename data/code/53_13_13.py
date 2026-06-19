from typing import Any

class Square:
    MIN_SIDE_LENGTH = 0.0
    
    def __init__(self, side_length: float):
        if side_length <= self.MIN_SIDE_LENGTH:
            raise ValueError("Side length must be greater than zero")
        self.side_length = side_length
    
    def calculate_area(self) -> float:
        return self.side_length ** 2

def main():
    try:
        side_length = 5.0
        square = Square(side_length)
        area = square.calculate_area()
        print(f"Area of the square with side length {side_length} is: {area}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
from typing import Dict

class Square:
    def __init__(self, side_length: float):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def get_area(self) -> float:
        return self.side_length ** 2

if __name__ == '__main__':
    square_sizes: Dict[str, float] = {
        'tiny': 1.5,
        'small': 3.0,
        'medium': 5.0,
        'large': 7.0
    }

    for size, length in square_sizes.items():
        square = Square(length)
        print(f"The area of a {size} square with side length {length} is {square.get_area()}")
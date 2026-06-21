from typing import TypeVar

T = TypeVar('T', int, float)

class Square:
    def __init__(self, side_length: T):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def get_area(self) -> T:
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_values = {
        'small': 3,
        'medium': 7,
        'large': 10
    }
    for size, value in sample_values.items():
        square = Square(value)
        print(f"The area of a {size} square with side length {value} is {square.get_area()}")
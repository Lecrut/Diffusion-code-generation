from typing import Dict

class Square:
    def __init__(self, side_length: float):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def get_area(self) -> float:
        return self.side_length * self.side_length

if __name__ == '__main__':
    sample_values: Dict[str, float] = {
        'tiny': 1.0,
        'small': 3.0,
        'medium': 7.0,
        'large': 10.0
    }
    
    for size, value in sample_values.items():
        square = Square(value)
        print(f"The area of a {size} square with side length {value} is {square.get_area()}")
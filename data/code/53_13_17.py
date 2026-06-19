from typing import Union
DEFAULT_SIDE_LENGTH = 5.0

class ShapeCalculator:

    def __init__(self, side_length: float):
        if side_length <= 0:
            raise ValueError('Side length must be positive')
        self.side_length = side_length

    def calculate_area(self) -> float:
        return self.side_length ** 2

def main():
    try:
        calculator = ShapeCalculator(DEFAULT_SIDE_LENGTH)
        area = calculator.calculate_area()
        print(area)
    except ValueError as e:
        print(e)
if __name__ == '__main__':
    main()
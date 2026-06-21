from typing import Final
DEFAULT_SIDE_LENGTH: Final[float] = 5.0

def calculate_area(side_length: float) -> float:
    return side_length * side_length

class ShapeAreaCalculator:

    def __init__(self, side_length: float):
        self.side_length = side_length

    def get_area(self) -> float:
        return calculate_area(self.side_length)
if __name__ == '__main__':
    area_calculator = ShapeAreaCalculator(DEFAULT_SIDE_LENGTH)
    area = area_calculator.get_area()
    print(area)
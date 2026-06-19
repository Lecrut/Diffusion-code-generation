from typing import Tuple

class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        self.sides: Tuple[float, float, float] = (side1, side2, side3)
    
    def perimeter(self) -> float:
        return sum(self.sides)

if __name__ == '__main__':
    first_side = 6.0
    second_side = 8.0
    third_side = 10.0
    triangle = Triangle(first_side, second_side, third_side)
    print(triangle.perimeter())
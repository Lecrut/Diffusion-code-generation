from typing import Tuple

class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        self.sides: Tuple[float, float, float] = (side1, side2, side3)
    
    def perimeter(self) -> float:
        return sum(self.sides)

if __name__ == '__main__':
    side_a = 7.0
    side_b = 8.0
    side_c = 9.0
    triangle_instance = Triangle(side_a, side_b, side_c)
    print(triangle_instance.perimeter())
from typing import Union

class Triangle:

    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> float:
        return self.side1 + self.side2 + self.side3
if __name__ == '__main__':
    SIDE_A: float = 6.0
    SIDE_B: float = 8.0
    SIDE_C: float = 10.0
    triangle_instance = Triangle(SIDE_A, SIDE_B, SIDE_C)
    print(triangle_instance.perimeter())
from typing import Tuple

class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        if any(side < 0 for side in (side1, side2, side3)):
            raise ValueError("Side lengths cannot be negative.")
        self.sides = (side1, side2, side3)

    def perimeter(self) -> float:
        return sum(self.sides)

def calculate_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    triangle = Triangle(side1, side2, side3)
    return triangle.perimeter()

if __name__ == '__main__':
    try:
        triangle = Triangle(3.0, 4.0, 5.0)
        print(triangle.perimeter())
        
        another_triangle = Triangle(7.5, 9.2, 6.8)
        print(another_triangle.perimeter())
    except ValueError as e:
        print(e)
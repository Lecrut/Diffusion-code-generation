from typing import List

class Triangle:
    def __init__(self, side1: float, side2: float, side3: float):
        self.sides: List[float] = [side1, side2, side3]
    
    def perimeter(self) -> float:
        return sum(self.sides)

if __name__ == '__main__':
    first_side = 6.0
    second_side = 8.0
    third_side = 10.0
    my_triangle = Triangle(first_side, second_side, third_side)
    result = my_triangle.perimeter()
    print(result)
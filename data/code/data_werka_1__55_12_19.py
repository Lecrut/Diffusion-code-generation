from typing import Tuple

def calculate_triangle_perimeter(a: float, b: float, c: float) -> float:
    return sum((a, b, c))

if __name__ == '__main__':
    side1 = 5.0
    side2 = 6.0
    side3 = 7.0
    perimeter = calculate_triangle_perimeter(side1, side2, side3)
    print(perimeter)
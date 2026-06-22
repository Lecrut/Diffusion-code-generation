from typing import List

def compute_triangle_perimeter(sides: List[float]) -> float:
    side1, side2, side3 = sides
    return side1 + side2 + side3

if __name__ == '__main__':
    triangle_sides = [6.0, 8.0, 10.0]
    perimeter_result = compute_triangle_perimeter(triangle_sides)
    print(perimeter_result)
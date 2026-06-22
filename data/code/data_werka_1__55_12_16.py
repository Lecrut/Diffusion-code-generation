from typing import List

def calculate_perimeter(triangle_sides: List[float]) -> float:
    if len(triangle_sides) != 3:
        raise ValueError("Exactly three sides are required to form a triangle.")
    side_a, side_b, side_c = triangle_sides
    if not (side_a > 0 and side_b > 0 and side_c > 0):
        raise ValueError("All sides must be positive numbers.")
    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        raise ValueError("The sum of any two sides must be greater than the third side.")
    return side_a + side_b + side_c

if __name__ == '__main__':
    sample_sides = [3.0, 4.0, 5.0]
    perimeter = calculate_perimeter(sample_sides)
    print(perimeter)
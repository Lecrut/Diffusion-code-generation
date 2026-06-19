from typing import List

def compute_triangle_perimeter(sides: List[float]) -> float:
    side_a, side_b, side_c = sides
    perimeter = side_a + side_b + side_c
    return perimeter

if __name__ == '__main__':
    sample_sides = [7.0, 24.0, 25.0]
    triangle_perimeter = compute_triangle_perimeter(sample_sides)
    print(triangle_perimeter)
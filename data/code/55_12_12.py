from typing import List

def compute_triangle_perimeter(sides: List[float]) -> float:
    if len(sides) != 3:
        raise ValueError("Exactly three sides are required.")
    
    side_a, side_b, side_c = sides
    
    if not (side_a > 0 and side_b > 0 and side_c > 0):
        raise ValueError("All sides must be positive numbers.")
    
    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        raise ValueError("The sum of any two sides must be greater than the third side.")
    
    return side_a + side_b + side_c

if __name__ == '__main__':
    sample_sides: List[float] = [7.0, 24.0, 25.0]
    try:
        perimeter: float = compute_triangle_perimeter(sample_sides)
        print(perimeter)
    except ValueError as e:
        print(e)
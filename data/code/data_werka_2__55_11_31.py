from typing import List

def calculate_triangle_perimeter(sides: List[float]) -> float:
    if len(sides) != 3:
        raise ValueError("A triangle must have exactly three sides.")
    
    side_a, side_b, side_c = sides
    
    if any(side <= 0 for side in sides):
        raise ValueError("All sides must be positive numbers.")
    
    if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
        raise ValueError("The sum of any two sides must be greater than the third side.")
    
    return side_a + side_b + side_c

if __name__ == '__main__':
    sample_sides: List[float] = [9.0, 12.0, 15.0]
    try:
        perimeter: float = calculate_triangle_perimeter(sample_sides)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")
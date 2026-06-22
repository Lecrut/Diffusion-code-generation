from typing import List

def validate_triangle_sides(sides: List[float]) -> None:
    if len(sides) != 3:
        raise ValueError("A triangle must have exactly three sides.")
    for side in sides:
        if side <= 0:
            raise ValueError("All sides must be positive numbers.")
    a, b, c = sides
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("The sum of any two sides must be greater than the third side.")

def calculate_triangle_perimeter(sides: List[float]) -> float:
    validate_triangle_sides(sides)
    return sum(sides)

if __name__ == '__main__':
    sample_sides: List[float] = [9.0, 12.0, 15.0]
    try:
        perimeter: float = calculate_triangle_perimeter(sample_sides)
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")
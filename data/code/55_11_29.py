from typing import List
NUM_SIDES = 3

def validate_triangle_sides(sides: List[float]) -> None:
    if len(sides) != NUM_SIDES:
        raise ValueError('A triangle must have exactly three sides.')
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError('All sides must be positive numbers.')
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError('The sum of any two sides must be greater than the third side.')

def calculate_triangle_perimeter(sides: List[float]) -> float:
    validate_triangle_sides(sides)
    return sum(sides)
if __name__ == '__main__':
    sample_sides1: List[float] = [9.0, 12.0, 15.0]
    try:
        perimeter1: float = calculate_triangle_perimeter(sample_sides1)
        print(perimeter1)
    except ValueError as e:
        print(f'Error: {e}')
    sample_sides2: List[float] = [7.0, 8.0, 9.0]
    try:
        perimeter2: float = calculate_triangle_perimeter(sample_sides2)
        print(perimeter2)
    except ValueError as e:
        print(f'Error: {e}')
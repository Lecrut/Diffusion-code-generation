from typing import Dict

def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    return side_a + side_b + side_c

def validate_triangle_sides(sides: Dict[str, float]) -> None:
    if sides['side_a'] <= 0 or sides['side_b'] <= 0 or sides['side_c'] <= 0:
        raise ValueError("All sides must be positive numbers.")
    if (sides['side_a'] + sides['side_b'] <= sides['side_c']) or \
       (sides['side_a'] + sides['side_c'] <= sides['side_b']) or \
       (sides['side_b'] + sides['side_c'] <= sides['side_a']):
        raise ValueError("The sum of any two sides must be greater than the third side.")

if __name__ == '__main__':
    sample_sides: Dict[str, float] = {
        'side_a': 9.0,
        'side_b': 12.0,
        'side_c': 15.0
    }
    
    try:
        validate_triangle_sides(sample_sides)
        perimeter: float = calculate_triangle_perimeter(
            sample_sides['side_a'],
            sample_sides['side_b'],
            sample_sides['side_c']
        )
        print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")
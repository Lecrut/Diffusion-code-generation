from typing import Dict

def compute_perimeter_of_triangle(sides: Dict[str, float]) -> float:
    return sum(sides.values())

if __name__ == '__main__':
    sample_sides: Dict[str, float] = {'side_a': 3.0, 'side_b': 4.0, 'side_c': 5.0}
    perimeter: float = compute_perimeter_of_triangle(sample_sides)
    print(perimeter)
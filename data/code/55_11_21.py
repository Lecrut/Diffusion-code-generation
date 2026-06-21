from typing import Dict

def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> float:
    return side_a + side_b + side_c

if __name__ == '__main__':
    sample_sides: Dict[str, float] = {
        'side_a': 6.0,
        'side_b': 8.0,
        'side_c': 10.0
    }
    perimeter: float = calculate_triangle_perimeter(
        sample_sides['side_a'],
        sample_sides['side_b'],
        sample_sides['side_c']
    )
    print(perimeter)
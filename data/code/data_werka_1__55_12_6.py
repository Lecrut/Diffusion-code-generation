from typing import Mapping

def calculate_triangle_perimeter(sides: Mapping[str, float]) -> float:
    return sum(sides.values())

if __name__ == '__main__':
    sample_sides = {'a': 3.0, 'b': 4.0, 'c': 5.0}
    perimeter = calculate_triangle_perimeter(sample_sides)
    print(perimeter)
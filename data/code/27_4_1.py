from typing import Tuple, List

def is_valid_triangle(a: int, b: int, c: int) -> bool:
    return a + b > c and a + c > b and b + c > a

def validate_triangles(configurations: List[Tuple[int, int, int]]) -> List[Tuple[Tuple[int, int, int], bool]]:
    results = []
    for sides in configurations:
        a, b, c = sides
        results.append((sides, is_valid_triangle(a, b, c)))
    return results

if __name__ == '__main__':
    sample_data = [
        (3, 4, 5),
        (1, 2, 3),
        (10, 10, 10),
        (1, 1, 100),
        (5, 5, 9)
    ]
    evaluation_results = validate_triangles(sample_data)
    for sides, valid in evaluation_results:
        print(f"Sides {sides}: {valid}")
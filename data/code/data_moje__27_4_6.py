from typing import Tuple, Union, Optional

def validate_triangle(a: float, b: float, c: float) -> Optional[str]:
    if a <= 0 or b <= 0 or c <= 0:
        return None
    if a + b <= c or a + c <= b or b + c <= a:
        return None
    if a == b and b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"

def evaluate_configurations(configurations: list[Tuple[float, float, float]]) -> None:
    results: list[Union[Tuple[float, float, float, str], Tuple[float, float, float, None]]] = []
    for side_a, side_b, side_c in configurations:
        triangle_type = validate_triangle(side_a, side_b, side_c)
        results.append((side_a, side_b, side_c, triangle_type))
    for result in results:
        print(result)

if __name__ == '__main__':
    test_cases: list[Tuple[float, float, float]] = [
        (3, 4, 5),
        (1, 1, 1),
        (2, 2, 5),
        (0, 4, 4),
        (6, 6, 6),
        (5, 5, 8),
        (1.5, 2.5, 3.0)
    ]
    evaluate_configurations(test_cases)
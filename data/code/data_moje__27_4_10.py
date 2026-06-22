from typing import List, Tuple

def is_valid_triangle(side_a: float, side_b: float, side_c: float) -> bool:
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return False
    return (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a)

def evaluate_triangles(configurations: List[Tuple[float, float, float]]) -> List[bool]:
    results = []
    for config in configurations:
        side_a, side_b, side_c = config
        results.append(is_valid_triangle(side_a, side_b, side_c))
    return results

if __name__ == '__main__':
    configs: List[Tuple[float, float, float]] = [
        (3.0, 4.0, 5.0),
        (1.0, 2.0, 3.0),
        (5.0, 5.0, 5.0),
        (-1.0, 4.0, 5.0),
        (0.0, 0.0, 0.0)
    ]
    outcomes = evaluate_triangles(configs)
    for outcome in outcomes:
        print(outcome)
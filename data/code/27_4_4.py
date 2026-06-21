from typing import Tuple, List, Optional

def validate_triangle(sides: Tuple[float, float, float]) -> Optional[bool]:
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

def check_configurations(configurations: List[Tuple[float, float, float]]) -> List[Tuple[Tuple[float, float, float], Optional[bool]]]:
    results: List[Tuple[Tuple[float, float, float], Optional[bool]]] = []
    for config in configurations:
        result = validate_triangle(config)
        results.append((config, result))
    return results

if __name__ == '__main__':
    sample_configs: List[Tuple[float, float, float]] = [
        (3.0, 4.0, 5.0),
        (1.0, 2.0, 10.0),
        (0.0, 5.0, 5.0),
        (7.0, 7.0, 7.0),
        (2.5, 2.5, 5.0)
    ]
    evaluations = check_configurations(sample_configs)
    for sides, is_valid in evaluations:
        print(f"Sides: {sides}, Valid: {is_valid}")
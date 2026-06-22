from typing import Tuple, List

def is_valid_triangle(sides: Tuple[float, float, float]) -> bool:
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)

def evaluate_configurations(configurations: List[Tuple[float, float, float]]) -> List[Tuple[Tuple[float, float, float], bool]]:
    results = []
    for config in configurations:
        results.append((config, is_valid_triangle(config)))
    return results

if __name__ == '__main__':
    sample_configs = [
        (3.0, 4.0, 5.0),
        (1.0, 2.0, 3.0),
        (5.0, 5.0, 5.0),
        (1.0, 1.0, 10.0),
        (0.0, 4.0, 4.0),
        (-1.0, 4.0, 4.0)
    ]
    output = evaluate_configurations(sample_configs)
    for config, valid in output:
        print(f"Triangle with sides {config} is valid: {valid}")
from typing import List, Tuple

def check_triangle_validity(sides: List[Tuple[float, float, float]]) -> List[bool]:
    results = []
    for a, b, c in sides:
        if a <= 0 or b <= 0 or c <= 0:
            results.append(False)
            continue
        if (a + b > c) and (a + c > b) and (b + c > a):
            results.append(True)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    configurations: List[Tuple[float, float, float]] = [
        (3, 4, 5),
        (1, 2, 3),
        (5, 5, 5),
        (0, 4, 4),
        (-1, 2, 2),
        (10, 21, 8)
    ]
    outcomes = check_triangle_validity(configurations)
    for config, is_valid in zip(configurations, outcomes):
        print(f"Sides {config} is {'valid' if is_valid else 'invalid'}")
from typing import Tuple

def is_valid_triangle(sides: Tuple[float, float, float]) -> bool:
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

if __name__ == '__main__':
    configurations = [
        (3, 4, 5),
        (1, 1, 10),
        (7, 7, 7),
        (0, 5, 5),
        (2.5, 3.5, 4.0)
    ]
    results = []
    for config in configurations:
        results.append(is_valid_triangle(config))
    print(results)
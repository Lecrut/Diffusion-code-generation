from typing import Tuple

def is_valid_triangle(sides: Tuple[float, float, float]) -> bool:
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True

if __name__ == '__main__':
    test_cases = [(3, 4, 5), (1, 2, 3), (10, 10, 10), (5, 1, 1), (0, 4, 5)]
    results = []
    for case in test_cases:
        result = is_valid_triangle(case)
        results.append(f"{case}: {result}")
    for line in results:
        print(line)
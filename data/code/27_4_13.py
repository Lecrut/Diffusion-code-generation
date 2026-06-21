from typing import Tuple, Optional

def is_valid_triangle(a: int, b: int, c: int) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True

def classify_triangle(a: int, b: int, c: int) -> Optional[str]:
    if not is_valid_triangle(a, b, c):
        return None
    if a == b and b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"

def check_configuration(sides: Tuple[int, int, int]) -> str:
    a, b, c = sides
    result = classify_triangle(a, b, c)
    if result is None:
        return f"Sides {sides} do not form a valid triangle."
    return f"Sides {sides} form a {result} triangle."

if __name__ == '__main__':
    configurations = [
        (3, 4, 5),
        (1, 1, 1),
        (2, 2, 5),
        (5, 12, 13),
        (7, 7, 7),
        (8, 5, 3)
    ]
    for config in configurations:
        print(check_configuration(config))
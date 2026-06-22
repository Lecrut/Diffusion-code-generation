from typing import List, Tuple, Union
import math

TriangleSides = Tuple[Union[int, float], Union[int, float], Union[int, float]]

def check_triangle_validity(a: float, b: float, c: float) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True

def calculate_triangle_type(a: float, b: float, c: float) -> str:
    if not check_triangle_validity(a, b, c):
        return "Invalid"
    if a == b == c:
        return "Equilateral"
    if a == b or b == c or a == c:
        return "Isosceles"
    return "Scalene"

def get_triangle_properties(a: float, b: float, c: float) -> dict:
    is_valid = check_triangle_validity(a, b, c)
    triangle_type = calculate_triangle_type(a, b, c)
    perimeter = a + b + c if is_valid else 0.0
    semi_perimeter = perimeter / 2 if is_valid else 0.0
    area = 0.0
    if is_valid:
        area = math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
    return {
        "valid": is_valid,
        "type": triangle_type,
        "perimeter": perimeter,
        "area": area
    }

def evaluate_configurations(configs: List[Tuple[float, float, float]]) -> List[dict]:
    results = []
    for side_a, side_b, side_c in configs:
        result = get_triangle_properties(side_a, side_b, side_c)
        result["sides"] = (side_a, side_b, side_c)
        results.append(result)
    return results

if __name__ == '__main__':
    sample_configs: List[Tuple[float, float, float]] = [
        (3, 4, 5),
        (1, 1, 1),
        (2, 2, 5),
        (7, 10, 5),
        (0, 4, 5),
        (6.5, 6.5, 6.5)
    ]
    evaluation_results = evaluate_configurations(sample_configs)
    for item in evaluation_results:
        print(f"Sides: {item['sides']}, Valid: {item['valid']}, Type: {item['type']}, Perimeter: {item['perimeter']}, Area: {item['area']}")
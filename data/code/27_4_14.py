from typing import Tuple, List, Union

def is_valid_triangle(sides: Tuple[float, float, float]) -> bool:
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a

def classify_triangle(sides: Tuple[float, float, float]) -> str:
    a, b, c = sides
    if not is_valid_triangle(sides):
        return "invalid"
    if a == b == c:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    return "scalene"

def evaluate_triangles(configurations: List[Tuple[float, float, float]]) -> List[str]:
    results: List[str] = []
    for sides in configurations:
        is_valid = is_valid_triangle(sides)
        if is_valid:
            category = classify_triangle(sides)
            results.append(f"{category} triangle")
        else:
            results.append("not a valid triangle")
    return results

if __name__ == "__main__":
    sample_configs: List[Tuple[float, float, float]] = [
        (3.0, 4.0, 5.0),
        (1.0, 1.0, 1.0),
        (2.0, 2.0, 5.0),
        (0.0, 1.0, 2.0),
        (7.0, 24.0, 25.0)
    ]
    outputs: List[str] = evaluate_triangles(sample_configs)
    for line in outputs:
        print(line)
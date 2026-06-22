from typing import List, Tuple, Union

def check_triangle_validity(sides: Tuple[Union[int, float], Union[int, float], Union[int, float]]) -> bool:
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

def evaluate_triangles(configurations: List[Tuple[Union[int, float], Union[int, float], Union[int, float]]]) -> List[bool]:
    results = []
    for sides in configurations:
        results.append(check_triangle_validity(sides))
    return results

if __name__ == '__main__':
    triangle_configs = [
        (3, 4, 5),
        (1, 2, 3),
        (7, 10, 5),
        (0, 4, 5),
        (-3, 4, 5),
        (1, 1, 1)
    ]
    results = evaluate_triangles(triangle_configs)
    print(results)
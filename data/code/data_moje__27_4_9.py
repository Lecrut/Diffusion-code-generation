def is_valid_triangle(a: float, b: float, c: float) -> bool:
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

def evaluate_triangles(sides: list[tuple[float, float, float]]) -> list[tuple[tuple[float, float, float], bool]]:
    results = []
    for side_tuple in sides:
        a, b, c = side_tuple
        valid = is_valid_triangle(a, b, c)
        results.append((side_tuple, valid))
    return results

if __name__ == '__main__':
    sample_sides = [
        (3.0, 4.0, 5.0),
        (1.0, 1.0, 2.0),
        (7.0, 10.0, 5.0),
        (-1.0, 2.0, 3.0),
        (0.0, 5.0, 5.0),
        (10.0, 2.0, 3.0)
    ]
    results = evaluate_triangles(sample_sides)
    for sides, is_valid in results:
        print(f"{sides}: {is_valid}")
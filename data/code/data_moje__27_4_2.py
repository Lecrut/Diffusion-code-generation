def is_valid_triangle(a: float, b: float, c: float) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def evaluate_triangles(triangles: list[tuple[float, float, float]]) -> list[bool]:
    results = []
    for a, b, c in triangles:
        results.append(is_valid_triangle(a, b, c))
    return results

if __name__ == '__main__':
    sample_triangles = [
        (3, 4, 5),
        (1, 2, 3),
        (7, 10, 5),
        (-1, 2, 3),
        (0, 5, 5),
        (10, 10, 10)
    ]
    results = evaluate_triangles(sample_triangles)
    for i, result in enumerate(results):
        print(f"Triangle {i + 1}: {sample_triangles[i]} -> {result}")
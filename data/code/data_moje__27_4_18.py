def evaluate_triangles(sides: list[tuple[float, float, float]]) -> list[bool]:
    results: list[bool] = []
    for a, b, c in sides:
        if a <= 0 or b <= 0 or c <= 0:
            results.append(False)
        elif a + b <= c or a + c <= b or b + c <= a:
            results.append(False)
        else:
            results.append(True)
    return results

if __name__ == '__main__':
    test_cases: list[tuple[float, float, float]] = [
        (3, 4, 5),
        (1, 2, 3),
        (7, 10, 5),
        (0, 4, 5),
        (-1, 2, 3),
        (1, 1, 1)
    ]
    results: list[bool] = evaluate_triangles(test_cases)
    print(results)
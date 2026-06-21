def evaluate_triangle_validity(sides: list[float]) -> dict[str, object]:
    if len(sides) != 3:
        return {'valid': False, 'error': 'Exactly three side lengths are required.'}
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return {'valid': False, 'error': 'All side lengths must be positive.'}
    if a + b <= c or a + c <= b or b + c <= a:
        return {'valid': False, 'error': 'The sides do not satisfy the triangle inequality theorem.'}
    return {'valid': True, 'error': None}
if __name__ == '__main__':
    sample_sides = [[3, 4, 5], [1, 2, 3], [7, 10, 5], [0, 4, 5], [-1, 2, 3], [10, 2, 5], [5, 5, 5], [3, 3, 3], [1, 1, 1], [2, 2, 3]]
    for sides in sample_sides:
        result = evaluate_triangle_validity(sides)
        print(f"Sides {sides} -> Valid: {result['valid']}, Error: {result['error']}")
def check_triangle_validity(side_sets):
    results = []
    for sides in side_sets:
        if len(sides) != 3:
            results.append(False)
            continue
        a, b, c = sorted(sides)
        is_positive = all(s > 0 for s in sides)
        satisfies_triangle_inequality = a + b > c
        results.append(is_positive and satisfies_triangle_inequality)
    return results

if __name__ == '__main__':
    sample_side_sets = [
        [3, 4, 5],
        [1, 2, 3],
        [10, 1, 1],
        [-1, 2, 3],
        [0, 0, 0],
        [5, 5, 5],
        [7, 10, 5]
    ]
    print(check_triangle_validity(sample_side_sets))
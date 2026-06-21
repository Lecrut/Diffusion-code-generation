def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sorted(sides)
    return a + b > c

def check_triangle_sets(sets):
    results = []
    for sides in sets:
        results.append(is_valid_triangle(sides))
    return results

if __name__ == '__main__':
    sample_sets = [
        [3, 4, 5],
        [1, 2, 3],
        [7, 10, 5],
        [10, 2, 1],
        [5, 5, 5],
        [0, 0, 0]
    ]
    print(check_triangle_sets(sample_sets))
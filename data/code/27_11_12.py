def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def check_triangle_sets(sets):
    results = []
    for side_set in sets:
        results.append(is_valid_triangle(side_set))
    return results

if __name__ == '__main__':
    sample_sets = [
        [3, 4, 5],
        [1, 2, 3],
        [7, 8, 9],
        [2, 2, 4],
        [10, 10, 10],
        [-1, 2, 3],
        [1, 1, 100]
    ]
    output = check_triangle_sets(sample_sets)
    print(output)
def check_valid_triangle_sets(sides_list):
    results = []
    for sides in sides_list:
        if len(sides) != 3:
            results.append(False)
            continue
        a, b, c = sides
        if a <= 0 or b <= 0 or c <= 0:
            results.append(False)
            continue
        if a + b > c and a + c > b and b + c > a:
            results.append(True)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    sample_sides = [
        (3, 4, 5),
        (1, 2, 3),
        (7, 10, 5),
        (0, 4, 5),
        (2, 2, 2),
        (1, 10, 12),
        (5, 12, 13)
    ]
    print(check_valid_triangle_sets(sample_sides))
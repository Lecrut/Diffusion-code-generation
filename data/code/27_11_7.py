def check_triangle_validity(side_sets):
    results = []
    for sides in side_sets:
        a, b, c = sides
        valid = (a > 0 and b > 0 and c > 0 and
                 a + b > c and
                 a + c > b and
                 b + c > a)
        results.append(valid)
    return results

if __name__ == '__main__':
    sample_sets = [
        (3, 4, 5),
        (1, 2, 3),
        (10, 10, 10),
        (1, 1, 3),
        (5, 5, 8)
    ]
    print(check_triangle_validity(sample_sets))
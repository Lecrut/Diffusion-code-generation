def determine_valid_triangles(side_length_sets):
    results = []
    for sides in side_length_sets:
        if len(sides) != 3:
            results.append(False)
            continue
        a, b, c = sorted(sides)
        if a > 0 and b > 0 and c > 0 and a + b > c:
            results.append(True)
        else:
            results.append(False)
    return results

if __name__ == '__main__':
    sample_sets = [
        [3, 4, 5],
        [1, 2, 3],
        [10, 15, 20],
        [1, 1, 1],
        [0, 5, 5],
        [-1, -2, -3],
        [2, 2, 4],
        [7, 24, 25]
    ]
    print(determine_valid_triangles(sample_sets))
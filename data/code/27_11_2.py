def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sorted(sides)
    return a + b > c

def check_triangle_validity_sets(side_sets):
    results = []
    for sides in side_sets:
        results.append(is_valid_triangle(sides))
    return results

if __name__ == '__main__':
    sample_data = [
        [3, 4, 5],
        [1, 2, 3],
        [5, 5, 5],
        [10, 2, 1],
        [7, 8, 9],
        [2, 2, 4]
    ]
    output = check_triangle_validity_sets(sample_data)
    print(output)
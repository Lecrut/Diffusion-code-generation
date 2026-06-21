def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sorted(sides)
    return a + b > c

if __name__ == '__main__':
    side_sets = [
        [3, 4, 5],
        [1, 2, 3],
        [5, 5, 5],
        [1, 1, 10],
        [2, 2, 3],
        [7, 24, 25]
    ]
    results = [is_valid_triangle(sides) for sides in side_sets]
    print(results)
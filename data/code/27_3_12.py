def is_valid_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c

if __name__ == '__main__':
    side_sets = [
        (3, 4, 5),
        (1, 2, 3),
        (5, 5, 5),
        (10, 1, 1)
    ]
    for sides in side_sets:
        result = is_valid_triangle(sides)
        print(f"{sides}: {result}")
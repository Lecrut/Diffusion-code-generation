def is_valid_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c and a > 0

if __name__ == '__main__':
    test_cases = [(3, 4, 5), (1, 2, 3), (7, 10, 5), (-1, 2, 3), (0, 0, 0)]
    for sides in test_cases:
        print(is_valid_triangle(sides))
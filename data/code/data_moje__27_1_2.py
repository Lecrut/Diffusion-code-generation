def is_valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and (b + c > a)
if __name__ == '__main__':
    test_cases = [(3, 4, 5), (1, 1, 1), (1, 2, 3), (7, 10, 5), (0, 5, 5), (-1, 2, 3), (1, 1, 2), (10, 10, 10)]
    for a, b, c in test_cases:
        result = is_valid_triangle(a, b, c)
        print(f'Triangle({a}, {b}, {c}): {result}')
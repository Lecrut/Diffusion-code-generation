def is_valid_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    test_cases = [(3, 4, 5), (1, 2, 3), (0, 1, 1), (5, 5, 5), (-1, 2, 3)]
    for sides in test_cases:
        result = is_valid_triangle(*sides)
        print(result)
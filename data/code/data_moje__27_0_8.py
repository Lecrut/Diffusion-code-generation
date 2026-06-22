def is_valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

if __name__ == '__main__':
    test_cases = [
        (3, 4, 5),
        (1, 2, 3),
        (7, 10, 5),
        (1, 1, 1),
        (0, 5, 5),
        (-1, 2, 3)
    ]
    for a, b, c in test_cases:
        result = is_valid_triangle(a, b, c)
        print(result)
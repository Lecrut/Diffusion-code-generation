def is_valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True

if __name__ == '__main__':
    test_cases = [
        (3, 4, 5),
        (1, 2, 3),
        (10, 5, 2),
        (7, 7, 7),
        (0, 4, 5)
    ]
    for sides in test_cases:
        result = is_valid_triangle(*sides)
        print(f"{sides}: {result}")
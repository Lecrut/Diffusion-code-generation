def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    test_cases = [
        (3, 4, 5),
        (1, 2, 3),
        (5, 10, 15),
        (7, 10, 15),
        (0, 0, 0),
        (2.5, 3.5, 4.5)
    ]
    for sides in test_cases:
        result = is_valid_triangle(*sides)
        print(result)
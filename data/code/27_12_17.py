def check_triangle(a, b, c):
    sides = sorted((a, b, c))
    return (a > 0) and (b > 0) and (c > 0) and (sides[0] + sides[1] > sides[2])

if __name__ == '__main__':
    test_cases = [
        (3, 4, 5),
        (0, 0, 0),
        (1, 2, 3),
        (-1, 2, 3),
        (7, 10, 5),
        (2, 2, 4),
        (10, 20, 25)
    ]
    for t in test_cases:
        print(check_triangle(*t))
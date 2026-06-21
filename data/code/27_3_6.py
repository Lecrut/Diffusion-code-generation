def is_valid_triangle(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    test_cases = [
        (3, 4, 5),
        (1, 2, 3),
        (10, 10, 10),
        (0, 0, 0),
        (1, 10, 12)
    ]
    results = []
    for sides in test_cases:
        results.append(is_valid_triangle(sides))
    print(results)
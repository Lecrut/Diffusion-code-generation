def check_triangle_validity(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0

if __name__ == '__main__':
    test_cases = (3, 4, 5), (1, 2, 3), (7, 2, 2), (5, 5, 5), (0, 1, 1)
    results = []
    for sides in test_cases:
        result = check_triangle_validity(sides)
        results.append(result)
    print(results)
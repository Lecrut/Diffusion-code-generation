def is_valid_triangle(a, b, c):
    return a > 0 and b > 0 and (c > 0) and (a + b > c) and (a + c > b) and (b + c > a)
if __name__ == '__main__':
    test_cases = [(3, 4, 5), (1, 2, 3), (0, 0, 0), (-1, 2, 3), (10, 2, 3)]
    for side_a, side_b, side_c in test_cases:
        result = is_valid_triangle(side_a, side_b, side_c)
        print(result)
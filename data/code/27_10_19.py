def is_valid_triangle(sides):
    a, b, c = sides
    return a + b > c and a + c > b and b + c > a and all(side > 0 for side in sides)

if __name__ == '__main__':
    test_cases = [(3.0, 4.0, 5.0), (1.0, 2.0, 3.0), (0.5, 0.5, 1.5), (-1.0, 4.0, 5.0), (2.5, 2.5, 2.5)]
    for case in test_cases:
        print(is_valid_triangle(case))
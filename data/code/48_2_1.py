def can_form_triangle(sides):
    if not isinstance(sides, list) or len(sides) != 3:
        return False
    a, b, c = sorted(sides)
    return a + b > c

if __name__ == '__main__':
    test_cases = [[3, 4, 5], [1, 2, 3], [5, 5, 5], [10, 1, 1]]
    for sides in test_cases:
        print(can_form_triangle(sides))
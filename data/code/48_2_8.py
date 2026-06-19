def can_form_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sorted(sides)
    return a + b > c
if __name__ == '__main__':
    sample_values = [[3, 4, 5], [1, 2, 3], [5, 5, 5], [10, 1, 1], [7, 10, 5]]
    for sides in sample_values:
        print(can_form_triangle(sides))
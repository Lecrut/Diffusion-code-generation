def can_form_triangle(sides):
    if any((side <= 0 for side in sides)):
        return False
    a, b, c = sorted(sides)
    return a + b > c
if __name__ == '__main__':
    sample_values = [[3, 4, 5], [1, 1, 2], [0, 4, 5], [-1, 4, 5], [7, 10, 5]]
    for sides in sample_values:
        print(can_form_triangle(sides))
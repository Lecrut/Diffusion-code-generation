def can_form_triangle(sides):
    if len(sides) != 3:
        raise ValueError('Exactly three sides are required to form a triangle.')
    a, b, c = sides
    if any((side <= 0 for side in (a, b, c))):
        raise ValueError('All sides must be positive numbers.')
    return a + b > c and a + c > b and (b + c > a)
if __name__ == '__main__':
    sample_values = [[3, 4, 5], [1, 1, 2], [0, 1, 1], [-1, 1, 1], [5, 5, 5], [7, 10, 5], [6, 6, 6], [8, 15, 17], [1, 2, 3], [0, 4, 5], [-3, 4, 5]]
    for sides in sample_values:
        try:
            print(can_form_triangle(sides))
        except ValueError as e:
            print(f'Error: {e}')
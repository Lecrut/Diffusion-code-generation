def can_form_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    is_valid_triangle = a + b > c and a + c > b and (b + c > a)
    return is_valid_triangle
if __name__ == '__main__':
    sample_values = [[3, 4, 5], [1, 1, 2], [0, 1, 1], [-1, 1, 1], [5, 5, 5], [7, 10, 5], [6, 6, 6], [8, 15, 17], [1, 1, 2], [0, 5, 5], [-3, 4, 5]]
    for sides in sample_values:
        print(can_form_triangle(sides))
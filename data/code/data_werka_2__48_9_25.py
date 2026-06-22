def can_form_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if any((x <= 0 for x in (a, b, c))):
        return False
    return a + b > c and a + c > b and (b + c > a)
if __name__ == '__main__':
    sample_values = [[3, 4, 5], [1, 2, 3], [0, 4, 5], [-1, 4, 5], [5, 5, 5], [2, 2, 3], [7, 10, 5], [8, 15, 17]]
    for sides in sample_values:
        print(can_form_triangle(sides))
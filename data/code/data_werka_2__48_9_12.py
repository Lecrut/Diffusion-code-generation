def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if any((x <= 0 for x in (a, b, c))):
        return False
    return a + b > c and a + c > b and (b + c > a)
if __name__ == '__main__':
    sample_values = [[3, 4, 5], [1, 1, 2], [0, 1, 1], [-1, 1, 1], [5, 5, 5], [2, 2, 3]]
    for sides in sample_values:
        print(is_valid_triangle(sides))
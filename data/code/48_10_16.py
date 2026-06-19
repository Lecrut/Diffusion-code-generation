def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    if any((side <= 0 for side in sides)):
        return False
    sorted_sides = sorted(sides)
    a, b, c = sorted_sides
    return a + b > c
if __name__ == '__main__':
    sample_values = [[6, 8, 10], [5, 5, 5], [2, 2, 3], [1, 2, 3], [7, 10, 5], [0, 4, 5], [-1, 4, 5]]
    for sides in sample_values:
        print(is_valid_triangle(sides))
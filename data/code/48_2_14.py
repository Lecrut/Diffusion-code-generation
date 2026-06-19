def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    a, b, c = sorted(sides)
    return a + b > c
if __name__ == '__main__':
    sample_values = [[3, 4, 5], [1, 2, 3], [7, 10, 5], [5, 5, 5], [10, 1, 1]]
    for sides in sample_values:
        print(is_valid_triangle(sides))
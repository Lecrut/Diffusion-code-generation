def is_valid_triangle(sides):
    if any((side <= 0 for side in sides)):
        return False
    a, b, c = sorted(sides)
    return a + b > c
if __name__ == '__main__':
    sample_values = [[3, 4, 5], [1, 2, 3], [0, 4, 5], [-1, 4, 5], [5, 5, 5], [2, 2, 4]]
    for sides in sample_values:
        print(is_valid_triangle(sides))
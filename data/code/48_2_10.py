def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    sides.sort()
    return sides[0] + sides[1] > sides[2]
if __name__ == '__main__':
    sample_values = [[3, 4, 5], [1, 2, 3], [5, 5, 5], [10, 1, 1]]
    for sides in sample_values:
        print(is_valid_triangle(sides))
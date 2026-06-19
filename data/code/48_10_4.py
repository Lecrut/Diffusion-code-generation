def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    sides = sorted(sides)
    return sides[0] > 0 and sides[1] > 0 and sides[2] > 0 and sides[0] + sides[1] > sides[2]

if __name__ == '__main__':
    sample_values = [[3, 4, 5], [1, 2, 3], [0, 4, 5], [-1, 4, 5], [5, 5, 5], [2, 2, 4]]
    for sides in sample_values:
        print(is_valid_triangle(sides))
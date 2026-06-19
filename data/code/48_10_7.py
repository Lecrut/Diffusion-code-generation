def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    for side in sides:
        if side <= 0:
            return False
    sides.sort()
    return sides[0] + sides[1] > sides[2]
if __name__ == '__main__':
    sample_values = [[3, 4, 5], [1, 2, 3], [0, 4, 5], [-1, 4, 5], [5, 5, 5], [2, 2, 4]]
    for sides in sample_values:
        print(is_valid_triangle(sides))
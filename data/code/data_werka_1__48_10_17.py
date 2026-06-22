def is_valid_triangle(sides):
    if len(sides) != 3:
        return False
    sides.sort()
    return all(side > 0 for side in sides) and sides[0] + sides[1] > sides[2]

if __name__ == '__main__':
    sample_values = [[6, 8, 10], [5, 7, 9], [0, 5, 7], [-2, 4, 6], [3, 3, 3], [4, 4, 8]]
    for sides in sample_values:
        print(is_valid_triangle(sides))
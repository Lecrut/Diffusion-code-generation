def is_valid_triangle(a, b, c):
    sides = sorted([a, b, c])
    return sides[0] > 0 and sides[0] + sides[1] > sides[2]

if __name__ == '__main__':
    print(is_valid_triangle(3, 4, 5))
    print(is_valid_triangle(1, 2, 3))
    print(is_valid_triangle(-1, 2, 3))
    print(is_valid_triangle(0, 0, 0))
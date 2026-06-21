def is_valid_triangle(a, b, c):
    if not (a > 0 and b > 0 and c > 0):
        return False
    sides = sorted([a, b, c])
    return sides[0] + sides[1] > sides[2]

if __name__ == '__main__':
    print(is_valid_triangle(3, 4, 5))
    print(is_valid_triangle(1, 2, 3))
    print(is_valid_triangle(-1, 5, 5))
    print(is_valid_triangle(0, 0, 0))
MIN_SIDE = 1
VALID = True
INVALID = False

def is_valid_triangle(a, b, c):
    if a < MIN_SIDE or b < MIN_SIDE or c < MIN_SIDE:
        return INVALID
    sorted_sides = sorted((a, b, c))
    return sorted_sides[0] + sorted_sides[1] > sorted_sides[2]

if __name__ == '__main__':
    print(is_valid_triangle(3, 4, 5))
    print(is_valid_triangle(1, 1, 1))
    print(is_valid_triangle(1, 2, 3))
    print(is_valid_triangle(10, 10, 20))
    print(is_valid_triangle(7, 7, 7))
    print(is_valid_triangle(0.5, 0.5, 0.5))
def validate_triangle(a, b, c):
    sides = (a, b, c)
    if any(s <= 0 for s in sides):
        return False
    return all(sides[i] + sides[j] > sides[k] for i, j, k in [(0, 1, 2), (0, 2, 1), (1, 2, 0)])

if __name__ == '__main__':
    print(validate_triangle(3, 4, 5))
    print(validate_triangle(1, 2, 3))
    print(validate_triangle(7, 10, 5))
    print(validate_triangle(-1, 2, 3))
    print(validate_triangle(0, 5, 5))
def triangle_sides_positive(a, b, c):
    positive = a > 0
    positive = positive and b > 0
    positive = positive and c > 0
    return positive

def is_valid_triangle(s1, s2, s3):
    if not triangle_sides_positive(s1, s2, s3):
        return False
    sides = [s1, s2, s3]
    sides.sort()
    return sides[0] + sides[1] > sides[2]

if __name__ == '__main__':
    print(is_valid_triangle(3, 4, 5))
    print(is_valid_triangle(1, 2, 3))
    print(is_valid_triangle(-1, 2, 3))
    print(is_valid_triangle(0, 5, 5))
    print(is_valid_triangle(7, 10, 5))
    print(is_valid_triangle(1, 1, 1))
    print(is_valid_triangle(10, 2, 2))
    print(is_valid_triangle(5, 5, 10))
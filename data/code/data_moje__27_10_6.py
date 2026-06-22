def is_valid_triangle(t):
    return t[0] + t[1] > t[2] and t[0] + t[2] > t[1] and t[1] + t[2] > t[0]

if __name__ == '__main__':
    print(is_valid_triangle((3.0, 4.0, 5.0)))
    print(is_valid_triangle((1.0, 2.0, 3.0)))
    print(is_valid_triangle((10.0, 1.0, 1.0)))
    print(is_valid_triangle((0.0, 0.0, 0.0)))
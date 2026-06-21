def is_valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and (b + c > a)
if __name__ == '__main__':
    print(is_valid_triangle(3, 4, 5))
    print(is_valid_triangle(1, 2, 3))
    print(is_valid_triangle(-1, 2, 3))
    print(is_valid_triangle(0, 1, 1))
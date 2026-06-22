def is_valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    s1, s2, s3 = 3, 4, 5
    print(is_valid_triangle(s1, s2, s3))
def check_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    return True

if __name__ == '__main__':
    print(check_triangle(3, 4, 5))
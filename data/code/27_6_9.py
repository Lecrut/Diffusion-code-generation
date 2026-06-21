def check_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"
    if a + b > c and a + c > b and b + c > a:
        return "Valid"
    return "Invalid"

if __name__ == '__main__':
    print(check_triangle(3, 4, 5))
    print(check_triangle(1, 2, 3))
    print(check_triangle(-1, 2, 3))
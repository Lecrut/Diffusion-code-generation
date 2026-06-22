def check_triangle_status(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"
    return "Valid"

if __name__ == '__main__':
    print(check_triangle_status(3, 4, 5))
    print(check_triangle_status(1, 2, 3))
    print(check_triangle_status(-1, 2, 3))
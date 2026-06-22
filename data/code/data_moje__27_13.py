def is_valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    a = 3
    b = 4
    c = 5
    result = is_valid_triangle(a, b, c)
    print(result)
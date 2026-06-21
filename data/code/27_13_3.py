def is_valid_triangle(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return False
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    result = is_valid_triangle(3, 4, 5)
    print(result)
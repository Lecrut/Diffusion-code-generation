def is_valid_triangle(a, b, c):
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True

if __name__ == '__main__':
    result = is_valid_triangle(3.0, 4.0, 5.0)
    print(result)
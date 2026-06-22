def is_valid_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True

if __name__ == '__main__':
    side1 = 3.0
    side2 = 4.0
    side3 = 5.0
    result = is_valid_triangle(side1, side2, side3)
    print(result)
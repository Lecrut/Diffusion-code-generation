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
    side1 = 3
    side2 = 4
    side3 = 5
    result = is_valid_triangle(side1, side2, side3)
    print(result)
    side4 = 1
    side5 = 2
    side6 = 3
    result = is_valid_triangle(side4, side5, side6)
    print(result)
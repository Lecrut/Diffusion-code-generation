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
    side_a = 3
    side_b = 4
    side_c = 5
    result = is_valid_triangle(side_a, side_b, side_c)
    print(result)
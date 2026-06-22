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
    val_a = 3.0
    val_b = 4.0
    val_c = 5.0
    result = is_valid_triangle(val_a, val_b, val_c)
    print(result)
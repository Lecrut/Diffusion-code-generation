def is_valid_triangle(a: float, b: float, c: float) -> bool:
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
    sides_1 = (3.0, 4.0, 5.0)
    sides_2 = (1.0, 2.0, 10.0)
    sides_3 = (5.0, 5.0, 5.0)
    result_1 = is_valid_triangle(*sides_1)
    result_2 = is_valid_triangle(*sides_2)
    result_3 = is_valid_triangle(*sides_3)
    print(result_1)
    print(result_2)
    print(result_3)
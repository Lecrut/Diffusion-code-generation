def is_valid_triangle(sides: tuple[float, float, float]) -> bool:
    a, b, c = sides
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
    sample_1 = (3.0, 4.0, 5.0)
    sample_2 = (1.0, 2.0, 3.0)
    sample_3 = (-1.0, 4.0, 5.0)
    print(is_valid_triangle(sample_1))
    print(is_valid_triangle(sample_2))
    print(is_valid_triangle(sample_3))
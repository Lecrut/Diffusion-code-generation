def validate_input(a: int, b: int, c: int) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a >= 100 or b >= 100 or c >= 100:
        return False
    if (a | 1) != a or (b | 1) != b or (c | 1) != c:
        return False
    return True

if __name__ == '__main__':
    print(validate_input(2, 4, 6))
    print(validate_input(1, 2, 4))
    print(validate_input(2, 4, 100))
    print(validate_input(0, 4, 6))
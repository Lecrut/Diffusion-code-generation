def validate_input(a, b, c):
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        raise ValueError("All inputs must be integers.")
    if a < 0 or a >= 100 or a % 2 != 0:
        return False
    if b < 0 or b >= 100 or b % 2 != 0:
        return False
    if c < 0 or c >= 100 or c % 2 != 0:
        return False
    return True

if __name__ == '__main__':
    print(validate_input(10, 20, 30))
    print(validate_input(100, 20, 30))
    print(validate_input(5, 10, 99))
    print(validate_input(10, 21, 30))
    print(validate_input(4, 68, 98))
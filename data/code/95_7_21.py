def validate_conditions(a, b, c):
    if a <= 0:
        return False
    if b % 2 != 0:
        return False
    divisor = a * b
    if divisor == 0:
        return False
    return c % divisor == 0

if __name__ == '__main__':
    print(validate_conditions(3, 2, 6))
    print(validate_conditions(3, 2, 7))
    print(validate_conditions(-1, 2, 2))
    print(validate_conditions(2, 3, 6))
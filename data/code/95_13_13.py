def validate_input(a: int, b: int, c: int) -> bool:
    return all(0 < x < 100 and (x & 1) == 0 for x in (a, b, c))

if __name__ == '__main__':
    print(validate_input(2, 4, 6))
    print(validate_input(2, 4, 100))
    print(validate_input(2, 3, 4))
    print(validate_input(-2, 4, 6))
def validate_input(a, b, c):
    return all(x > 0 and x < 100 and (x & 1) == 0 for x in (a, b, c))

if __name__ == '__main__':
    print(validate_input(2, 4, 6))
    print(validate_input(0, 4, 6))
    print(validate_input(2, 3, 6))
    print(validate_input(2, 4, 100))
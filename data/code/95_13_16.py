def validate_input(a, b, c):
    return (a & 1 == 0) and (b & 1 == 0) and (c & 1 == 0) and (a > 0) and (b > 0) and (c > 0) and (a < 100) and (b < 100) and (c < 100)

if __name__ == '__main__':
    print(validate_input(4, 68, 98))
    print(validate_input(100, 20, 30))
    print(validate_input(5, 10, 99))
    print(validate_input(10, 21, 30))
MAX_VALUE = 100

def validate_input(a, b, c):
    return all(x > 0 and x % 2 == 0 and x < MAX_VALUE for x in (a, b, c))

if __name__ == '__main__':
    print(validate_input(4, 68, 98))
    print(validate_input(100, 20, 30))
    print(validate_input(5, 10, 99))
    print(validate_input(10, 21, 30))
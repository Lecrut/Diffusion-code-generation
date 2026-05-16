def check_equality(a, b):
    return a == b
if __name__ == '__main__':
    x = 10
    y = 10
    print(check_equality(x, y))
    x = [1, 2]
    y = [1, 2]
    print(check_equality(x, y))
    x = 10
    y = 20
    print(check_equality(x, y))
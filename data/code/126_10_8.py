def check_equality(a, b):
    return a == b
if __name__ == '__main__':
    print(check_equality(None, None))
    print(check_equality(1, 1))
    print(check_equality(1.0, 1))
    print(check_equality('hello', 'hello'))
    print(check_equality('hello', 'world'))
    print(check_equality(None, 1))
def check_equality(a, b):
    return a == b
if __name__ == '__main__':
    print(check_equality(None, None))
    print(check_equality(1, 2))
    print(check_equality(3.0, 3))
    print(check_equality('hello', 'hello'))
    print(check_equality('hello', 'world'))
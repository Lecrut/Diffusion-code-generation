def check_equality(a, b):
    if a is None or b is None:
        return a == b
    else:
        return a is b and a == b
if __name__ == '__main__':
    print(check_equality(None, None))
    print(check_equality(10, 10))
    print(check_equality('hello', 'hello'))
    print(check_equality([], []))
    print(check_equality({}, {}))
    print(check_equality(None, 0))
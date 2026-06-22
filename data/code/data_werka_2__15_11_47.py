def check_equality(a, b):
    if a is None or b is None:
        return a == b
    else:
        return a is b
if __name__ == '__main__':
    value1 = 42
    value2 = 42
    value3 = None
    value4 = None
    value5 = 'hello'
    value6 = 'world'
    print(check_equality(value1, value2))
    print(check_equality(value3, value4))
    print(check_equality(value1, value3))
    print(check_equality(value5, value6))
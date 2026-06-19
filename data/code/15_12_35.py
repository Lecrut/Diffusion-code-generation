def check_equality(a, b):
    if a is None and b is None:
        return True
    elif a is None or b is None:
        return False
    else:
        return a == b
if __name__ == '__main__':
    value1 = None
    value2 = None
    value3 = 5
    value4 = 'hello'
    print(check_equality(value1, value2))
    print(check_equality(value1, value3))
    print(check_equality(value3, value3))
    print(check_equality(value4, value4))
    print(check_equality(value3, value4))
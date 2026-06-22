def check_equality(a, b):
    if a is None and b is None:
        return True
    elif a is None or b is None:
        return False
    else:
        return a == b
if __name__ == '__main__':
    print(check_equality(None, None))
    print(check_equality(10, 10))
    print(check_equality('hello', 'hello'))
    print(check_equality([1, 2], [1, 2]))
    print(check_equality(None, 0))
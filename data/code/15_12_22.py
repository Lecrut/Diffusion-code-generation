def check_equality(a, b):
    if a is None and b is None:
        return True
    elif a is None or b is None:
        return False
    else:
        return a == b
if __name__ == '__main__':
    print(check_equality(None, None))
    print(check_equality(None, 0))
    print(check_equality(1, 1))
    print(check_equality('a', 'a'))
    print(check_equality([], []))